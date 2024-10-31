# Примеры

  
Python имеет встроенную поддержку SQLite базы данных, для этого вам не надо ничего дополнительно устанавливать, достаточно в скрипте указать импорт стандартной библиотеки:
```python
import sqlite3
```    

- Скачаем тестовую базу данных, с которой будем работать. В данной статье будет использоваться открытая (MIT лицензия) тестовая база данных “Chinook”. Скачать ее можно с репозитория:  
- [github.com/lerocha/chinook-database](https://github.com/lerocha/chinook-database) 
- бинарный файл [Chinook_Sqlite.sqlite](https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite)  
    
- Для удобства работы с базой (просмотр, редактирование) нам нужна программа браузер баз данных, поддерживающая SQLite. В статье работа с браузером не рассматривается, но он поможет Вам наглядно видеть что происходит с базой в процессе наших экспериментов.  
    **Примечание**: внося изменения в базу не забудьте их применить, так как база с непримененными изменениями остается залоченной.  
    Вы можете использовать (последние два варианта кросс-платформенные и бесплатные):  
    - Привычную вам утилиту для работы с базой в составе вашей IDE;
    - [SQLite Database Browser](http://sqlitebrowser.org/)
    - [SQLiteStudio](https://sqlitestudio.pl/index.rvt)

```python
# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

# Не забываем закрыть соединение с базой данных
conn.close()
```

### 0. Смотрим базу данных

```python
### 0. Смотрим базу данных

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
# Получение списка всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Таблицы в базе данных:")
for table in tables:
	print(f"\nТаблица: {table[0]}")
	# Получение структуры таблицы
	cursor.execute(f"PRAGMA table_info({table[0]});")
	columns = cursor.fetchall()

	print("Структура таблицы:")
	for column in columns:
		print(f" - {column[1]} (Тип: {column[2]}, NULL: {column[3]}, Дефолт: {column[4]})")
	
	# Получение первых 5 записей из таблицы
	cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
	records = cursor.fetchall()

	print("Примеры записей:")
	for record in records:
		print(f" - {record}")
# Закрытие соединения
conn.close()
```

### 1. Создание и управление таблицами

- **Структура базы данных Chinook**: Объясните, какие таблицы имеются в базе (например, `albums`, `artists`, `customers`, `invoices`, `tracks`) и их связи.
- **Типы данных SQLite**: Пройдитесь по различным типам данных, использованным в таблицах, например, `INTEGER`, `TEXT`, `REAL`.

```python

import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Получаем список таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Таблицы в базе данных:")
for table in tables:
    print(table[0])

conn.close()
```

### 3. Вставка, обновление и удаление данных

- **Добавление данных**: Напишите пример вставки новых записей, например, добавление нового исполнителя или альбома.

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Добавление нового исполнителя
insert_artist_query = '''
INSERT INTO artists (Name) VALUES ('Новый Исполнитель')
'''
cursor.execute(insert_artist_query)
conn.commit()

print("Исполнитель добавлен.")
conn.close()
```
- **Обновление данных**: Показать, как обновить информацию о существующем исполнителе (например, изменить имя).

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Обновление имени исполнителя с ID = 1
update_artist_query = '''
UPDATE artists
SET Name = 'Обновленный Исполнитель'
WHERE ArtistId = 1
'''
cursor.execute(update_artist_query)
conn.commit()

print("Исполнитель обновлен.")
conn.close()
```

- **Удаление данных**: Пример удаления трека или альбома из базы данных.

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Удаление трека с ID = 1
delete_track_query = '''
DELETE FROM tracks
WHERE TrackId = 1
'''
cursor.execute(delete_track_query)
conn.commit()

print("Трек удален.")
conn.close()
```

### 4. Выполнение запросов

- **Извлечение данных**: Используйте операторы SELECT для выборки данных, например, получение всех треков определенного альбома.

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Получение всех треков определенного альбома (например, AlbumId = 1)
select_tracks_query = '''
SELECT Name FROM tracks WHERE AlbumId = 1
'''
cursor.execute(select_tracks_query)
tracks = cursor.fetchall()

print("Треки альбома:")
for track in tracks:
    print(track[0])

conn.close()
```

- **Фильтрация данных**: Используйте WHERE для поиска клиентов по стране или исполнителей по имени.

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Поиск клиентов из США
select_customers_query = '''
SELECT FirstName, LastName FROM customers WHERE Country = 'USA'
'''
cursor.execute(select_customers_query)
customers = cursor.fetchall()

print("Клиенты из США:")
for customer in customers:
    print(f"{customer[0]} {customer[1]}")

conn.close()
```

- **Группировка и сортировка**: Пример использования GROUP BY для подсчета количества альбомов у каждого исполнителя и ORDER BY для сортировки результатов.

```python
import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Подсчет количества альбомов у каждого исполнителя
group_query = '''
SELECT artists.Name, COUNT(albums.AlbumId) AS AlbumCount
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
GROUP BY artists.ArtistId
ORDER BY AlbumCount DESC
'''
cursor.execute(group_query)
results = cursor.fetchall()

print("Количество альбомов у исполнителей:")
for row in results:
    print(f"Исполнитель: {row[0]}, Альбомов: {row[1]}")

conn.close()
```

### 5. Обработка результатов

- **Получение результатов**: Показать, как извлекать данные из курсора и преобразовывать их в списки или словари.

```python
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
# Извлечение всех клиентов
select_customers_query = 'SELECT * FROM customer'
cursor.execute(select_customers_query)
customers = cursor.fetchall()
# Преобразование в словарь
customers_list = []
for customer in customers:
	customers_list.append({
	'CustomerId': customer[0],
	'FirstName': customer[1],
	'LastName': customer[2],
	'Country': customer[3],
	})
print(customers_list)
conn.close()
```

- **Работа с NULL**: Пример, как обрабатывать записи с отсутствующими данными.
```python
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
# Поиск исполнителей без альбомов
null_query = '''
SELECT Name FROM artist
WHERE ArtistId NOT IN (SELECT DISTINCT ArtistId FROM album)
'''
cursor.execute(null_query)
results = cursor.fetchall()
print("Исполнители без альбомов:")
for row in results:
	print(row[0])
conn.close()
```

### 6. Транзакции и управление данными

- **Понятие транзакций**: Объясните важность транзакций при работе с изменениями в базе данных.

```python
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

try:
	cursor = conn.cursor()
	cursor.execute('BEGIN')
	# Пример нескольких операций
	cursor.execute('INSERT INTO artist (Name) VALUES ("Транзакционный Исполнитель")')
	cursor.execute('INSERT INTO album (Title, ArtistId) VALUES ("Транзакционный Альбом", LAST_INSERT_ROWID())')
	conn.commit()
	print("Транзакция успешно выполнена.")
except Exception as e:
	conn.rollback()
	print("Произошла ошибка. Транзакция отменена:", e)
finally:
	conn.close()
```

- **Контекстные менеджеры**: Как использовать `with` для автоматического управления транзакциями.

```python
with sqlite3.connect('Chinook_Sqlite.sqlite') as conn:
	cursor = conn.cursor()
	cursor.execute('BEGIN')
	cursor.execute('INSERT INTO artist (Name) VALUES ("Исполнитель с контекстом")')
	cursor.execute('INSERT INTO album (Title, ArtistId) VALUES ("Альбом с контекстом", LAST_INSERT_ROWID())')
	# Если все прошло успешно, коммит произойдет автоматически при выходе из блока with
	print("Транзакция успешно выполнена с помощью контекстного менеджера.")
```

### 7. Продвинутые концепции

- **Подготовленные запросы**: Объясните, как использовать подготовленные запросы для защиты от SQL-инъекций и повышения производительности.

```python
import sqlite3

def get_connection(db_file):
    return sqlite3.connect(db_file)

def find_artist_by_name(connection, artist_name):
    cursor = connection.cursor()
    # Использование подготовленного запроса
    cursor.execute("SELECT ArtistId, Name FROM Artist WHERE Name = ?", (artist_name,))
    artist = cursor.fetchone()
    return artist
```

- **Создание представлений**: Пример создания представления для упрощения сложных запросов, например, общее представление продаж по исполнителям.

```python
def create_album_sales_view(connection):
    cursor = connection.cursor()
    # Удаление представления, если оно уже существует
    cursor.execute("DROP VIEW IF EXISTS AlbumSales")
    
    # Создание представления
    cursor.execute("""
        CREATE VIEW AlbumSales AS
        SELECT 
            a.AlbumId, 
            a.Title AS AlbumTitle, 
            ar.Name AS ArtistName, 
            COUNT(il.InvoiceLineId) AS TotalSales
        FROM 
            Album a
        JOIN 
            Artist ar ON a.ArtistId = ar.ArtistId
        LEFT JOIN 
            InvoiceLine il ON a.AlbumId = il.TrackId
        GROUP BY 
            a.AlbumId, ar.Name
    """)
    connection.commit()

def query_album_sales_view(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM AlbumSales")
    return cursor.fetchall()
```


--- 

#  1. Sqlite 
## 1.1: Запросить список всех клиентов и количество их заказов.
## 1.2 Найти все треки, которые были выпущены после 2010 года.
## 1.3 Создать представление для отображения общего количества продаж по каждому альбому.

# 2. ORM

В процессе разработки мы работаем с объектами различной природы, в то время как взаимодействие с SQL-базой данных требует постоянного формирования текстовых запросов, которые затем необходимо преобразовывать в формат данных, используемый в приложении.

Оптимальным решением было бы наличие механизма автоматического генерирования запросов на основе заранее определенной структуры данных, а также приведение ответов к этой же структуре. Такой механизм реализуется с помощью добавления ORM-прослойки между кодом приложения и SQL-базой данных.

Тем не менее, в высоконагруженных проектах использование такой прослойки может привести к дополнительным расходам ресурсов и требовать детальной настройки, что выходит за рамки данной работы.

Существует два основных подхода к реализации ORM:

1. **Active Record**: Этот подход является более простым для понимания и реализации. Он основывается на отображении объекта данных на строку таблицы базы данных.
    
2. **Data Mapper**: В отличие от предыдущего подхода, Data Mapper полностью разделяет представление данных в приложении и их представление в базе данных.
    

Каждый из этих подходов обладает своими особенностями, преимуществами и недостатками, что зависит от типа разрабатываемого приложения.


```python
import sqlite3

# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"

# Создание класса для представления исполнителя
class Artist:
    def __init__(self, artist_id, name):
        self.artist_id = artist_id
        self.name = name

    def __repr__(self):
        return f"Artist(id={self.artist_id}, name='{self.name}')"

# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)

# Функция для получения всех альбомов
def get_all_albums(connection):
	pass

# Функция для получения исполнителей
def get_all_artists(connection):
	pass

# Функция для получения треков, выпущенных после 2010 года
def get_tracks_after_2010(connection):
	pass

```

# 3. CRUD

В данной задаче вам необходимо ознакомиться с CRUD-операции с базами данных, включающие создание (Create), чтение (Read), обновление (Update) и удаление (Delete) объектов или записей. Основное внимание будет уделено базовым аспектам, которые позволят решить реальные задачи разработки.

Существует два основных подхода при работе с объектно-реляционными отображениями (ORM), которые зависят от целей и предпочтений разработчика:

1. **Использование общих методов модели**: В этом подходе осуществляется вызов методов класса модели, таких как `.select()`, `.update()`, `.delete()`, `.create()` и других. Этот метод позволяет выполнять массовые операции, передавая дополнительные параметры. Логика работы в данном случае аналогична выполнению SQL-запросов, однако, благодаря моделям, привязки к таблицам и известные поля уже имеются, что исключает необходимость их явного указания.
    
2. **Работа с экземплярами модели**: Второй подход предполагает получение объекта класса модели, который соответствует одной записи таблицы базы данных. С этим объектом возможно взаимодействие, включая изменение значений его атрибутов. По завершении работы изменения могут быть сохранены с помощью метода `.save()`, или запись может быть удалена с помощью метода `.delete_instance()`. Примеры CRUD-операций будут иллюстрировать эти подходы более наглядно.

```python
import sqlite3

# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"

# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)

# CRUD операции для альбомов

# 1. Создание (Create)
def create_album(connection, title, artist_id):
	pass

# 2. Чтение (Read)
def read_albums(connection):
	pass

# 3. Обновление (Update)
def update_album(connection, album_id, new_title):
	pass

# 4. Удаление (Delete)
def delete_album(connection, album_id):
	pass


```

## Полезные материалы 

- [Введение в базы данных](https://habr.com/ru/articles/686816/)
- Краткий бесплатный онлайн курс — [Udacity — Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
- [Advanced SQLite Usage in Python](http://pythoncentral.io/advanced-sqlite-usage-in-python/)  
- [SQLite Python Tutorial на tutorialspoint.com](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)  
- [A thorough guide to SQLite database operations in Python](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)  
- [The Novice's Guide to the Python 3 DB-API](http://www.philvarner.com/test/ng-python3-db-api/) 
- Справочные руководства по SQLite онлайн:  
    - [www.tutorialspoint.com/sql/index.htm](https://www.tutorialspoint.com/sql/index.htm)
    - [www.tutorialspoint.com/sqlite](https://www.tutorialspoint.com/sqlite/)
    - [www.sqlitetutorial.net](http://www.sqlitetutorial.net/)