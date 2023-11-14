# Курс: Информатика
#computer_science #python #note #vcs
# Практическое занятие №8. "Стратегии"

Теперь для успешной сдачи практического занятия по мимо выполнения задач из методички `note.md` необходимо набрать **$25$ баллов** из решения задач приведенных в `task.md` задачи имеют разную сложность и соответственно разную цену.

## Обязательные задачи

### 🐟
У вас есть списки морских и пресноводных рыб, оба упорядочены в алфавитном порядке.  Как создать из них один общий список, тоже отсортированный по алфавиту?

```python
sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"] 
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]
```

### 🌷 
В парфюмерии цветочные ароматы изготавливают путем комбинирования запахов различных цветов. Если дано множество цветов $F$, то как посчитать все ароматы, которые можно изготовить из них?

```python
`flowers_set = {"rose", "jasmine", "lily"}`
`flowers_set = {"orchid", "tulip", "violet", "daisy"}`
`flowers_set = {"lavender", "sunflower"}`
```

### 💰 
У вас есть список цен на золото по дням за какой-то интервал времени. В этом интервале вы хотите найти такие два дня, чтобы, купив золото, а затем продав его, вы получили бы максимально возможную прибыль.

```python
gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]
```

### 🎒 
У вас есть рюкзак, вы носите в нем предметы, которыми торгуете. Его вместимость ограничена определенным весом, так что вы не можете сложить в него весь свой товар. Вы должны выбрать, что взять. Цена и вес каждого предмета известны, вам нужно посчитать, какое их сочетание дает самый высокий доход.

```python
# 1. Вес предмета
# 2. Стоимость предмета

items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5

items_2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
weight_limit_2 = 10

items_3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
weight_limit_3 = 7

items_4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
weight_limit_4 = 7

items_5 = [(6, 10), (8, 15), (12, 30)]
weight_limit_5 = 5
```

### 👺 
Грабитель пробирается в ваш дом, чтобы украсть предметы, которые вы хотели продать. Он решает использовать ваш рюкзак, чтобы унести в нем украденное. Что он возьмет? Имейте в виду, что чем быстрее он уйдет, тем меньше вероятность, что его поймают с поличным.

```python
# 1. Стоимость предмета.
# 2. Время, которое грабитель тратит на укладку этого предмета в рюкзак.
# 3. Вес предмета.

items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

```
### 🙈

Реализовать сортировку слиянием (Merge Sort) с временной сложностью вида $O(n \space log n)$ и релизовать сортировку выбором (Selection Sort) с временной сложностью $O(n^2)$.

```python
import random
import time

# Реализация сортировки слиянием
def merge_sort(arr):
	# Ваша реализация 
    return merge(left, right)

def merge(left, right):
    result = []
	# Ваша реализация
	return result

# Реализация сортировки выбором
def selection_sort(arr):


# Функция для генерации случайного списка заданной длины
def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]

def test

# Сравнение эффективности алгоритмов на случайных списках разных размеров
for size in [100, 1000, 10000, 100000]:
    arr = generate_random_list(size)

    # Измерение времени выполнения сортировки слиянием
    start_time = time.time()
    merge_sort(arr.copy())
    merge_sort_time = time.time() - start_time

    # Измерение времени выполнения сортировки выбором
    start_time = time.time()
    selection_sort(arr.copy())
    selection_sort_time = time.time() - start_time

    print(f"Размер списка: {size}")
    print(f"Время выполнения сортировки слиянием: {merge_sort_time:.5f} сек")
    print(f"Время выполнения сортировки выбором: {selection_sort_time:.5f} сек")
    print("="*50)


if __name__ == "__main__":
	test()
```
# Балльные задания

## Упрощенный конечный автомат TCP (FSM) (15 баллов)

Автоматы, или конечные автоматы (FSM), чрезвычайно полезны программистам, когда дело касается разработки программного обеспечения. Вам будет предоставлена упрощенная версия FSM для кода базового сеанса TCP.

Результатом этого упражнения будет возврат правильного состояния TCP FSM на основе заданного массива событий.

Входной массив событий будет состоять из одной или нескольких следующих строк:
```
APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
```

Состояния следующие и должны быть указаны заглавными буквами, как показано:

```
CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
```

Входными данными будет массив событий. Исходное состояние `CLOSED`. Ваша задача — пройти конечный автомат в соответствии с событиями и вернуть правильное конечное состояние в виде строки с заглавными буквами, как показано выше.

Если событие неприменимо к текущему состоянию, ваш код вернет `ERROR`.

Действие каждого события на каждое состояние:

(формат `INITIAL_STATE: EVENT -> NEW_STATE`)

```
CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED
```

Примеры:
```
["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"] =>  "ESTABLISHED"

["APP_ACTIVE_OPEN"] =>  "SYN_SENT"

["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"] =>  "ERROR"
```

```python
def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    return "ESTABLISHED"
```

Тесты:
```python
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]), "CLOSE_WAIT")
traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"]), "ESTABLISHED")    
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]), "LAST_ACK")
traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","APP_SEND"]), "ERROR")
traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK",   "APP_CLOSE"]),"FIN_WAIT_1")
traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"]), "ESTABLISHED")
traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN"]), "SYN_RCVD")
traverse_TCP_states(["APP_PASSIVE_OPEN"]), "LISTEN")
traverse_TCP_states(["APP_ACTIVE_OPEN","APP_CLOSE"]), "CLOSED")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK"]), "TIME_WAIT")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK","APP_TIMEOUT"]), "CLOSED")
traverse_TCP_states(["RCV_SYN","RCV_ACK","APP_CLOSE"]),"ERROR")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_ACK"]), "FIN_WAIT_2")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]), "CLOSE_WAIT")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]), "LAST_ACK")
traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
traverse_TCP_states(["APP_PASSIVE_OPEN","APP_CLOSE"]), "CLOSED")
traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","APP_CLOSE"]), "FIN_WAIT_1")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_PASSIVE_OPEN"]), "ERROR")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_FIN_ACK","APP_TIMEOUT","APP_ACTIVE_OPEN","RCV_SYN","APP_CLOSE","RCV_FIN","RCV_ACK"]), "TIME_WAIT")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_SYN"]), "ERROR")
traverse_TCP_states(["APP_PASSIVE_OPEN","APP_CLOSE","RCV_SYN"]), "ERROR")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE"]), "FIN_WAIT_1")
traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","RCV_FIN"]), "CLOSING")

```
## Числа Хэмминга (10 баллов)

Число Хэмминга — это целое положительное число вида $2^i3^j5^k$ для некоторых неотрицательных целых чисел $i$, $j$ и $k$.

Напишите функцию, которая вычисляет $n$-ное наименьшее число Хэмминга.

Конкретно:

- Первое наименьшее число Хэмминга равно 1 = $2^03^05^0$.
- Второе наименьшее число Хэмминга — 2 = $2^13^05^0$.
- Третье наименьшее число Хэмминга равно 3 = $2^03^15^0$.
- Четвертое наименьшее число Хэмминга — 4 = $2^23^05^0$.
- Пятое наименьшее число Хэмминга — 5 = $2^03^05^1$.
 
20 наименьших чисел Хэмминга приведены в примере испытательного приспособления.

Ваш код должен быть в состоянии вычислить первые `5 000` чисел Хэмминга без тайм-аута.

```python
def hamming(n):
    pass
```
## Когда сумма делителей кратна сумме простых множителей (5 баллов)

Числа `12`, `63` и `119` имеют кое-что общее, связанное с их делителями и простыми множителями, давайте посмотрим.

```
Numbers PrimeFactorsSum(pfs)        DivisorsSum(ds)              Is ds divisible by pfs
12         2 + 2 + 3 = 7         1 + 2 + 3 + 4 + 6 + 12 = 28            28 / 7 = 4,  Yes
63         3 + 3 + 7 = 13        1 + 3 + 7 + 9 + 21 + 63 = 104         104 / 13 = 8, Yes
119        7 + 17 = 24           1 + 7 + 17 + 119 = 144                144 / 24 = 6, Yes
```

Вы можете увидеть очевидное свойство: сумма делителей числа делится на сумму его простых множителей.

Нам нужна функция `ds_multof_pfs()`, которая получает два аргумента: `nMin` и `nMax`, в качестве нижнего и верхнего предела (включительно) соответственно, и выводит отсортированный список с числами, удовлетворяющими описанному выше свойству.

Представляем особенности описываемой функции:

```python
ds_multof_pfs(nMin, nMax) -----> [n1, n2, ....., nl] # nMin ≤ n1 < n2 < ..< nl ≤ nMax
```

```python
ds_multof_pfs(10, 100) == [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]

ds_multof_pfs(20, 120) == [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
```

```python
def ds_multof_pfs(nMin, nMax):
    # your code here
    return [] # sorted list
```
## Перемещение нулей в конец (5 баллов)
Напишите алгоритм, который берет массив и перемещает все нули в конец, сохраняя порядок остальных элементов.

```python
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

```python
def move_zeros(lst):
    return lst
```

```python
assert_equals(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
assert_equals(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```
## Hashtag (5 баллов)
Задача заключается в создании генератора хэштегов для помощи маркетинговой команде, которая тратит слишком много времени на ввод хэштегов. Вот правила для создания хэштегов:

1. Хэштег должен начинаться с символа решетки (#).
2. Все слова в тексте должны начинаться с заглавной буквы.
3. Если итоговая строка хэштега длиннее 140 символов, функция должна вернуть "false".
4. Если входная строка или итоговая строка хэштега являются пустыми строками, функция также должна вернуть "false".
```python
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

```python
def generate_hashtag(s):
    pass
```

```python

```
## Две черепахи (5 баллов)
Задача: Два черепахи, названные `A` и `B`, участвуют в беговой гонке. Черепаха `A` начинает гонку с средней скоростью `720` футов в час. Молодая черепаха B знает, что она бегает быстрее, чем `A`, и к тому же не закончила свою капусту.

Когда она стартует, наконец, она видит, что `A` имеет преимущество в `70` футов, но скорость `B` составляет `850` футов в час. Сколько времени `B` потребуется, чтобы догнать `A`?

Более общая формулировка: учитывая две скорости `v1` (скорость `A`, целое число > 0) и `v2` (скорость `B`, целое число > 0) и преимущество `g` (целое число > 0), сколько времени потребуется `B`, чтобы догнать `A`?

Результат будет представлен в виде массива `[часы, минуты, секунды]` - это время в часах, минутах и секундах (округленное до ближайшей секунды) или строка в некоторых языках.

Если `v1` >= `v2`, то верните, None или `[-1, -1, -1]`.

Примеры: 
`race(720, 850, 70) => [0, 32, 18]` или `"0 32 18"` 
`race(80, 91, 37) => [3, 21, 49]` или `"3 21 49"`

## Сортировать по языку программирования (2 балла)

Вам будет предоставлен массив объектов, представляющих данные о разработчиках, которые зарегистрировались для участия в следующей конференции по программированию, которую вы организуете.

Учитывая следующий входной массив:
```python
list1 = [  
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]
```

Напишите функцию, которая возвращает массив, отсортированный в алфавитном порядке по языку программирования. Если есть разработчики, пишущие на том же языке, отсортируйте их в алфавитном порядке по имени:

```python
[ 
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" }
]
```

```python
def sort_by_language(arr):
    pass
```

Тестовые массивы
```python
        arr1 = [
          {"first_name": "Kseniya", "last_name": "A.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
          {"first_name": "Jing", "last_name": "X.", "country": "China", "continent": "Asia", "age": 39, "language": "Ruby" },
          {"first_name": "Andrei", "last_name": "E.", "country": "Romania", "continent": "Europe", "age": 59, "language": "C" },
          {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 60, "language": "C" },
          {"first_name": "Chloe", "last_name": "K.", "country": "Guernsey", "continent": "Europe", "age": 88, "language": "Ruby" },
          {"first_name": "Viktoria", "last_name": "W.", "country": "Bulgaria", "continent": "Europe", "age": 98, "language": "PHP" },
          {"first_name": "Piotr", "last_name": "B.", "country": "Poland", "continent": "Europe", "age": 128, "language": "JavaScript" }
        ]

        arr2 = [
          {"first_name": "Paulo", "last_name": "K.", "country": "Brazil", "continent": "Americas", "age": 19, "language": "Python" }
        ]

        arr3 = [  
          {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
          {"first_name": "Precious", "last_name": "G.", "country": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
          {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C" },
          {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
        ]

        arr4 = [  
          {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
          {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C" },
          {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
        ]

        arr5 = arr4 + arr3 
```

## Битовый счетчик наибольшего общего делителя (2 балла)

Цель состоит в том, чтобы написать метод, который принимает два целочисленных параметра и возвращает одно целое число, равное количеству единиц в двоичном представлении наибольшего общего делителя параметров.

Взято из Википедии: «В математике наибольший общий делитель (НОД) двух или более целых чисел, когда хотя бы одно из них не равно нулю, — это наибольшее положительное целое число, которое делит числа без остатка. Например, НОД числа 8 и 12 — это 4».

Например: наибольший общий делитель чисел 300 и 45 равен 15. Двоичное представление числа 15 равно 1111, поэтому правильным результатом будет 4.

Если оба параметра равны 0, метод должен вернуть 0. Функция должна иметь возможность обрабатывать отрицательные входные данные.

```python
def binary_gcd(x, y):
    return None
```

Тестовые данные 

```python
        binary_gcd(666666, 333111), 6)
        binary_gcd(545034,5), 1)
        binary_gcd(0, 0), 0)
        binary_gcd(0, 76899299), 14)
        binary_gcd(666666, 333111), 6)
        binary_gcd(-124, -16), 1)
```

## Пластмассовый баланс (2 балла)

Вы получите список с несколькими разбросанными номерами.

Вы должны убедиться, что сумма двух значений с обеих сторон равна сумме остальных элементов списка.

А если нет, удалите два элемента по бокам и проверьте еще раз,

пока не дойдете до контрольного списка условий:

Сумма списка без сторон = сумме сторон.

Если оно никогда не будет равно, верните пустой список
```python
[1,2,3,4,5] ==> 1+5 != 2+3+4 ==> [2,3,4] ==> 2+4 != 3 == [3] ==> 3+3 != 0 ==> []
```

```python
def plastic_balance(lst):
    return
```

Тестовые примеры:
```python
        plastic_balance([1,2,3,4,5]), []
        plastic_balance([0,104,3,101,0,111]), [104,3,101,0]
        plastic_balance([1,-1]), [1,-1]
        plastic_balance([0]), [0]
        plastic_balance([100,0,-100]), [100,0,-100]
        plastic_balance([4,4]), []
```