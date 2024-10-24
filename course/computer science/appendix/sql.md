# Введение
[`SQLite`](https://www.sqlite.org/download.html) - это, пожалуй, самая простая база данных, к которой можно подключиться с помощью `Python`-приложения, поскольку для этого не нужно устанавливать никаких внешних модулей `Python SQL`. По умолчанию инсталляция `Python` содержит библиотеку `Python SQL` под названием `sqlite3`, которую можно использовать для взаимодействия с базой данных `SQLite`.

> Документация https://docs.python.org/3/library/sqlite3.html

Более того, базы данных `SQLite` являются бессерверными и самодостаточными, поскольку они читают и записывают данные в файл. Это означает, что, в отличие от `MySQL` и `PostgreSQL`, для выполнения операций с базами данных даже не нужно устанавливать и запускать сервер `SQLite`!

Вот как можно использовать `sqlite3` для подключения к базе данных `SQLite` на языке `Python`:
```python
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
```

# Подключение к базе данных

Подключение к базе данных SQLite можно установить с помощью метода `connect()`, передав в качестве параметра имя базы данных, к которой необходимо получить доступ. Если такой базы данных не существует, то она будет создана.
```python
sqliteConnection = sqlite3.connect('sql.db')
```
Но что делать, если необходимо выполнить некоторые запросы после установления соединения. Для этого необходимо создать курсор с помощью метода `cursor()` на экземпляре соединения, который и будет выполнять наши SQL-запросы.

```python
cursor = sqliteConnection.cursor()
print('DB Init')
```

## Пример 
```python
import sqlite3

try:

	# Connect to DB and create a cursor
	sqliteConnection = sqlite3.connect('sql.db')
	cursor = sqliteConnection.cursor()
	print('DB Init')

	# Write a query and execute it with cursor
	query = 'select sqlite_version();'
	cursor.execute(query)

	# Fetch and output result
	result = cursor.fetchall()
	print('SQLite Version is {}'.format(result))

	# Close the cursor
	cursor.close()

# Handle errors
except sqlite3.Error as error:
	print('Error occurred - ', error)

# Close DB Connection irrespective of success
# or failure
finally:

	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')
```

# SQLite Datatypes
SQLite - это библиотека на языке Си, представляющая собой переносимый и бессерверный механизм баз данных SQL. Она имеет файловую архитектуру, поэтому читает и записывает данные на диск. Поскольку SQLite является базой данных с нулевой конфигурацией, перед ее использованием не требуется установка или настройка. Начиная с версии Python 2.5.x, SQLite3 поставляется с python по умолчанию.

## Класс хранилища в SQLite
Классом хранения можно назвать коллекцию однотипных DataTypes. В SQLite предусмотрены следующие классы хранения:

|Storage Class|Value Stored|
|---|---|
|NULL|NULL|
|INTEGER|Signed Integer (1, 2, 3, 4, 5, or 8 bytes depending on magnitude)|
|REAL|Floating point value (8 byte IEEE floating-point numbers)|
|TEXT|TEXT string (encoded in UTF-8, UTF-16BE or UTF-16LE|
|BLOB (Binary Large Object)|Data stored exactly the way it was input, generally in binary format|

## Соответствующие типы данных Python

|Storage Class|Python Datatype|
|---|---|
|NULL|None|
|INTEGER|int|
|REAL|float|
|TEXT|str|
|BLOB|bytes|

Функция type() может быть использована в python для получения класса аргумента. В приведенной ниже программе функция type() используется для вывода классов каждого значения, хранящегося в базе данных.

```python
# Python3 program to demonstrate SQLite3 datatypes 
# and corresponding Python3 types 

# import the sqlite3 package 
import sqlite3 

# create connection to database 
cnt = sqlite3.connect('gfg.db') 

# Create a exam_hall relation 
cnt.execute('''CREATE TABLE exam_hall( 
NAME TEXT, 
PIN INTEGER, 
OCCUPANCY REAL, 
LOGO BLOB);''') 

# Open the logo file in read, binary mode 
# read the image as binary data into a variable 
fileh = open('/images/lissajous.png', 'rb') 
img = fileh.read() 

# Insert tuples for the relation 
cnt.execute('''INSERT INTO exam_hall VALUES( 
'centre-a',1125,98.6,?)''', (img,)) 
cnt.execute('''INSERT INTO exam_hall VALUES( 
NULL,1158,80.5,?)''', (img,)) 

# Query the data, print the data and its type 
# note: Printing the image binary data is impractical due to its huge size 
# instead number of bytes are being printed using len() 
cursor = cnt.execute('''SELECT * FROM exam_hall;''') 
for i in cursor: 
	print(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(len(i[3]))) 
	print(str(type(i[0]))+" "+str(type(i[1]))+" " +
		str(type(i[2]))+" "+str(type(i[3]))+"\n") 

```

#  Cursor

Python-код для создания базы данных hotel_data и вставки записей в таблицу hotel.

```python
# importing sqlite3 module
import sqlite3


# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')

# query to create a table named FOOD1
connection.execute(''' CREATE TABLE hotel
		(FIND INT PRIMARY KEY	 NOT NULL,
		FNAME		 TEXT NOT NULL,
		COST		 INT	 NOT NULL,
		WEIGHT	 INT);
		''')

# insert query to insert food details in 
# the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )")
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )")
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )")


print("All data in food table\n")

# create a cousor object for select query
cursor = connection.execute("SELECT * from hotel ")

# display all data from hotel table
for row in cursor:
	print(row)
```
Python-код для отображения данных из таблицы отеля.
```python
# importing sqlite3 module
import sqlite3

# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')


# insert query to insert food details 
# in the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )");
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )");
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )");


print("Food id and Food Name\n")

# create a cousor object for select query
cursor = connection.execute("SELECT FIND,FNAME from hotel ")

# display all data from FOOD1 table
for row in cursor:
	print(row)

```

# SQLite – Create Table

В базе данных SQLite для создания таблицы используется следующий синтаксис:

```sql
CREATE TABLE database_name.table_name(
	column1 datatype PRIMARY KEY(one or more columns),
	column2 datatype,
	column3 datatype,
	  .......
	columnN datatype
);
```

Теперь мы создадим таблицу с помощью языка Python:

**Подход:**

Импортировать необходимый модуль

- Установите соединение или создайте объект соединения с базой данных с помощью функции connect() модуля sqlite3.
- Создать объект Cursor, вызвав метод cursor() объекта Connection.
- Сформировать таблицу с помощью оператора CREATE TABLE с использованием метода execute() класса Cursor.
```python
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE GEEK (
			Email VARCHAR(255) NOT NULL,
			First_Name CHAR(25) NOT NULL,
			Last_Name CHAR(25),
			Score INT
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()

```