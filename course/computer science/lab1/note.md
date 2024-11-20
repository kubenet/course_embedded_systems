# Курс: Информатика
#computer_science #python #lab 
# Лабораторная работа № 1 "Базы данных"


SQLAlchemy — это мощный инструмент для работы с реляционными базами данных (такими как SQLite, PostgreSQL, MySQL и другие), который предоставляет разработчикам удобные и гибкие средства для взаимодействия с базами данных. Знание SQLAlchemy необходимо каждому разработчику, работающему с реляционными базами данных, поскольку оно позволяет значительно упростить и стандартизировать процесс работы с данными.

### Модели таблиц

SQLAlchemy предоставляет возможность описывать структуру таблиц базы данных с помощью Python-классов, называемых **моделями таблиц**. Каждая модель определяет таблицу, её колонки и их типы данных. Таким образом, вместо работы с необработанными SQL-запросами, разработчик взаимодействует с базой данных через объектно-ориентированный подход, используя модели.

В рамках данной статьи мы рассмотрим основные типы колонок, включая распространённые (`Integer`, `String`, `Text`) и специализированные (`Array`, `JSON`).

Мы также изучим, как настроить связи между таблицами на уровне базы данных с помощью внешних ключей (`ForeignKey`) и организовать взаимодействие таблиц через механизм `relationship`. Это позволяет задавать типы связей, такие как:

- **"Один к одному" (1:1);**
- **"Один ко многим" (1:N)**;
- **"Многие к одному" (N:1)**.


После описания моделей создадим соответствующие таблицы с использованием инструмента **Alembic** — библиотеки для управления миграциями базы данных, которая хорошо интегрируется с SQLAlchemy. Это позволяет удобно вносить изменения в структуру базы данных, особенно в командной разработке.

---

### Теоретическая основа

SQLAlchemy — это не просто фреймворк, а полноценный инструмент для работы с реляционными базами данных. Он поддерживает два основных подхода:

- **Core** — низкоуровневый стиль, дающий полный контроль над SQL-запросами, что полезно для задач с особыми требованиями к производительности.
- **ORM (Object-Relational Mapping)** — высокоуровневый подход, который отображает таблицы базы данных на Python-классы. Работа с ORM позволяет оперировать объектами вместо SQL-запросов. Мы сосредоточимся на использовании ORM, так как этот подход более удобен и популярен.

---

### Основные компоненты ORM

Работа с SQLAlchemy в стиле ORM включает несколько ключевых понятий:

1. **Модели таблиц** — Python-классы, представляющие структуру таблиц базы данных, включая их колонки и связи.
2. **Сессии** — объекты, обеспечивающие взаимодействие с базой данных. Сессия позволяет выполнять запросы, фиксировать изменения и управлять подключением к базе.
3. **Фабрика сессий** — шаблон для создания новых сессий по мере необходимости, что особенно полезно при работе в многопоточных приложениях.

---

### Преимущества использования SQLAlchemy

SQLAlchemy существенно упрощает работу с базами данных, позволяя описывать структуры данных и выполнять запросы на языке Python, что делает код более читаемым и поддерживаемым. Кроме того, SQLAlchemy обеспечивает универсальность, позволяя легко переходить между различными СУБД с минимальными изменениями в коде.

---

### Организация связей между таблицами

SQLAlchemy предоставляет гибкие механизмы для работы с отношениями между таблицами:

- **"Один к одному" (1:1)** — каждая запись в одной таблице соответствует одной записи в другой. Пример: связь профиля пользователя с его учётной записью.
- **"Один ко многим" (1
    
    )** — одна запись в одной таблице может быть связана с несколькими записями в другой. Пример: один пользователь может иметь несколько заказов.
- **"Многие к одному" (N:1)** — несколько записей из одной таблицы ссылаются на одну запись в другой. Пример: несколько заказов могут быть привязаны к одному магазину.

Эти механизмы позволяют строить сложные структуры данных, сохраняя при этом удобство доступа к связанным данным.

# Цели:

1. Освоить создание ORM (Object-Relational Mapping) с помощью Python.
2. Написать базовые CRUD-операции для выбранной базы данных.
3. Подготовить код для последующего использования в:
    - GUI-приложении на PyQt или Tk.
    - Web-приложении на Flask с использованием REST API.

## Исходные данные:

- Используйте базу данных из [Kaggle](https://www.kaggle.com/datasets?fileType=sqlite) или базы, изученные на 8-м практическом занятии.

### Выбор базы данных

1. Выберите базу данных из предложенных источников:
    - [Kaggle](https://www.kaggle.com/datasets?fileType=sqlite).
    - Базы данных, изученные ранее.
2. Проанализируйте структуру данных: таблицы, связи, типы данных.

### Создание ORM

1. Установите библиотеку [SQLAlchemy](https://www.sqlalchemy.org/).
2. Напишите классы для таблиц базы данных:
    - Названия классов должны соответствовать таблицам.
    - Поля классов должны соответствовать колонкам таблиц.

#### Пример

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()

# Таблица Artist
class Artist(Base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Album
    albums = relationship('Album', back_populates='artist')

# Таблица Album
class Album(Base):
    __tablename__ = 'Album'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

    # Связь с таблицей Artist
    artist = relationship('Artist', back_populates='albums')
    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='album')

# Таблица Track
class Track(Base):
    __tablename__ = 'Track'
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('MediaType.MediaTypeId'))
    GenreId = Column(Integer, ForeignKey('Genre.GenreId'))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

    # Связи
    album = relationship('Album', back_populates='tracks')
    media_type = relationship('MediaType', back_populates='tracks')
    genre = relationship('Genre', back_populates='tracks')

# Таблица MediaType
class MediaType(Base):
    __tablename__ = 'MediaType'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='media_type')

# Таблица Genre
class Genre(Base):
    __tablename__ = 'Genre'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)

    # Связь один ко многим с таблицей Track
    tracks = relationship('Track', back_populates='genre')

# Таблица Customer
class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer, ForeignKey('Employee.EmployeeId'))

    # Связь с таблицей Employee
    support_rep = relationship('Employee', back_populates='customers')

# Таблица Employee
class Employee(Base):
    __tablename__ = 'Employee'
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('Employee.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)

    # Связь один ко многим с Customer
    customers = relationship('Customer', back_populates='support_rep')
    # Связь один ко многим с самим собой (менеджеры)
    subordinates = relationship('Employee', backref='manager', remote_side=[EmployeeId])

# Таблица Invoice
class Invoice(Base):
    __tablename__ = 'Invoice'
    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey('Customer.CustomerId'))
    InvoiceDate = Column(DateTime)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String)
    Total = Column(Float)

    # Связь с таблицей Customer
    customer = relationship('Customer', back_populates='invoices')

# Добавление связей, пропущенных ранее
Customer.invoices = relationship('Invoice', back_populates='customer')

# Настройка подключения к базе данных
def setup_database(database_path="sqlite:///Chinook_Sqlite.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


engine = setup_database("sqlite:///Chinook_Sqlite.sqlite") session = create_session(engine)
# Добавить нового артиста
new_artist = Artist(Name="New Artist")
session.add(new_artist)
session.commit()
print(f"Added artist with ID: {new_artist.ArtistId}")
# Получить все альбомы артиста 
artist = session.query(Artist).filter_by(Name="New Artist").first()
if artist:
    print(f"Albums by {artist.Name}: {[album.Title for album in artist.albums]}")
# Удалить трек
track = session.query(Track).filter_by(Name="Some Track").first()
if track:
    session.delete(track)
    session.commit()
    print("Track deleted.")
```

### Реализация CRUD-операций

1. Напишите функции для следующих операций:
    - Создание записи.
    - Чтение записи (по ID и всех записей).
    - Обновление записи.
    - Удаление записи.

#### Пример

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import setup_database, create_session, Artist, Album, Track  # Подключаем модели из ORM

# Инициализация базы данных
engine = setup_database("sqlite:///Chinook_Sqlite.sqlite")
session = create_session(engine)

# CREATE (Создание)
def add_artist(name):
    new_artist = Artist(Name=name)
    session.add(new_artist)
    session.commit()
    print(f"Artist '{name}' added with ID: {new_artist.ArtistId}")
    return new_artist.ArtistId

def add_album(title, artist_id):
    new_album = Album(Title=title, ArtistId=artist_id)
    session.add(new_album)
    session.commit()
    print(f"Album '{title}' added with ID: {new_album.AlbumId}")
    return new_album.AlbumId

def add_track(name, album_id, media_type_id, genre_id, composer, milliseconds, bytes_, unit_price):
    new_track = Track(
        Name=name,
        AlbumId=album_id,
        MediaTypeId=media_type_id,
        GenreId=genre_id,
        Composer=composer,
        Milliseconds=milliseconds,
        Bytes=bytes_,
        UnitPrice=unit_price
    )
    session.add(new_track)
    session.commit()
    print(f"Track '{name}' added with ID: {new_track.TrackId}")
    return new_track.TrackId

# READ (Чтение)
def get_artist_by_id(artist_id):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        print(f"Artist: {artist.Name}")
        return artist
    else:
        print(f"Artist with ID {artist_id} not found.")
        return None

def get_all_albums():
    albums = session.query(Album).all()
    for album in albums:
        print(f"Album ID: {album.AlbumId}, Title: {album.Title}")
    return albums

def get_tracks_by_album(album_id):
    tracks = session.query(Track).filter_by(AlbumId=album_id).all()
    print(f"Tracks in Album ID {album_id}:")
    for track in tracks:
        print(f"- {track.Name}")
    return tracks

# UPDATE (Обновление)
def update_artist_name(artist_id, new_name):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        artist.Name = new_name
        session.commit()
        print(f"Artist ID {artist_id} updated to '{new_name}'")
        return artist
    else:
        print(f"Artist with ID {artist_id} not found.")
        return None

def update_album_title(album_id, new_title):
    album = session.query(Album).filter_by(AlbumId=album_id).first()
    if album:
        album.Title = new_title
        session.commit()
        print(f"Album ID {album_id} updated to '{new_title}'")
        return album
    else:
        print(f"Album with ID {album_id} not found.")
        return None

# DELETE (Удаление)
def delete_artist(artist_id):
    artist = session.query(Artist).filter_by(ArtistId=artist_id).first()
    if artist:
        session.delete(artist)
        session.commit()
        print(f"Artist ID {artist_id} deleted.")
    else:
        print(f"Artist with ID {artist_id} not found.")

def delete_album(album_id):
    album = session.query(Album).filter_by(AlbumId=album_id).first()
    if album:
        session.delete(album)
        session.commit()
        print(f"Album ID {album_id} deleted.")
    else:
        print(f"Album with ID {album_id} not found.")

def delete_track(track_id):
    track = session.query(Track).filter_by(TrackId=track_id).first()
    if track:
        session.delete(track)
        session.commit()
        print(f"Track ID {track_id} deleted.")
    else:
        print(f"Track with ID {track_id} not found.")

# Примеры использования
if __name__ == "__main__":
    # Создание
    artist_id = add_artist("New Artist")
    album_id = add_album("New Album", artist_id)
    add_track("New Track", album_id, media_type_id=1, genre_id=1, composer="Composer", milliseconds=300000, bytes_=5000000, unit_price=0.99)

    # Чтение
    get_artist_by_id(artist_id)
    get_all_albums()
    get_tracks_by_album(album_id)

    # Обновление
    update_artist_name(artist_id, "Updated Artist")
    update_album_title(album_id, "Updated Album")

    # Удаление
    delete_track(1)  # Удаление трека по ID
    delete_album(album_id)
    delete_artist(artist_id)
```

# Полезные ссылки
---
[8 Практическая работа](../chapter8/note)
[Крадущийся тигр, затаившийся SQLAlchemy. Основы](https://habr.com/ru/articles/470285/)
[Менеджер контекста это просто](https://habr.com/ru/articles/739326/)
[DrawSQL](https://drawsql.app/templates/hacker-news)