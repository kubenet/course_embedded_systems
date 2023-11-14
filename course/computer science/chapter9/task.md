
Теперь для успешной сдачи практического занятия по мимо выполнения задач из методички `note.md` необходимо набрать **$25$ баллов** из решения задач приведенных в `task.md` задачи имеют разную сложность и соответственно разную цену.

# Обязательные задачи
## Stack

Вам необходимо реализовать `Stack` на языке Python, включая основные методы для манипуляции данными внутри стека. Ваша цель - создать класс Python с именем `Stack`:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):

    def push(self, item):

    def pop(self):

    def peek(self):

    def size(self):

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items)

# Pop an item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)

# Peek at the top of the stack
top_item = my_stack.peek()
print("Top item:", top_item)

# Check if the stack is empty
print("Is stack empty?", my_stack.is_empty())

# Get the size of the stack
print("Stack size:", my_stack.size())

```

## Queue

Вам необходимо реализовать `Queue` на языке Python, включая основные методы для манипуляции данными внутри `Queue`. Ваша цель - создать класс Python с именем `Queue`:

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):

    def enqueue(self, item):

    def dequeue(self):

    def front(self):

    def size(self):

my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue:", my_queue.items)

# Dequeue an item from the queue
dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)

# Get the front of the queue
front_item = my_queue.front()
print("Front item:", front_item)

# Check if the queue is empty
print("Is queue empty?", my_queue.is_empty())

# Get the size of the queue
print("Queue size:", my_queue.size())

```
## Linked List 

Вам необходимо реализовать `Linked List` на языке Python, включая основные методы для манипуляции данными внутри `Linked List`. Ваша цель - создать класс Python с именем `Linked List`:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):

    def append(self, data):

    def prepend(self, data):

    def delete(self, data):

    def display(self):



# Example usage:
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()
```
## Tree

Вам необходимо реализовать `Tree` на языке Python, включая основные методы для манипуляции данными внутри `Tree`. Ваша цель - создать класс Python с именем `Tree`:


```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):


    def _insert_recursive(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):


# Example usage:
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Inorder Traversal:", tree.inorder_traversal())

# Searching for a key
key_to_search = 40
result_node = tree.search(key_to_search)
if result_node:
    print(f"Key {key_to_search} found in the tree.")
else:
    print(f"Key {key_to_search} not found in the tree.")
```

## Unorder map

Вам необходимо реализовать `Unorder map` на языке Python, включая основные методы для манипуляции данными внутри `Unorder map`. Ваша цель - создать класс Python с именем `Unorder map`:

```python
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def set(self, key, value):

    def get(self, key, default=None):

    def remove(self, key):

    def keys(self):

    def values(self):

    def items(self):

my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())

```

## Unordered Set

Вам необходимо реализовать `Unorder Set` на языке Python, включая основные методы для манипуляции данными внутри `Unorder Set`. Ваша цель - создать класс Python с именем `Unorder Set`:

```python
class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):

    def add(self, value):

    def remove(self, value):

    def contains(self, value):

    def elements(self):

my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())
```

## Binary Tree

Вам необходимо реализовать `Binary Tree` на языке Python, включая основные методы для манипуляции данными внутри `Binary Tree`. Ваша цель - создать класс Python с именем  `Binary Tree`:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):

    def _insert(self, root, key):

    def search(self, key):

    def _search(self, root, key):

    def inorder_traversal(self):

    def _inorder_traversal(self, root, result):


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Inorder Traversal:", tree.inorder_traversal())

# Searching for a key
key_to_search = 40
result_node = tree.search(key_to_search)
if result_node:
    print(f"Key {key_to_search} found in the tree.")
else:
    print(f"Key {key_to_search} not found in the tree.")

```
## Hashmap

Вам необходимо реализовать `Hash Map` на языке Python, включая основные методы для манипуляции данными внутри `Hash Map`. Ваша цель - создать класс Python с именем `Hash Map`:

```python
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        # A simple hash function using the length of the key
        return 

    def put(self, key, value):
        hash_value = self._hash(key)


    def get(self, key, default=None):


    def remove(self, key):


    def keys(self):


    def values(self):


    def items(self):

my_hashmap = HashMap()

my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")

print("Keys:", my_hashmap.keys())
print("Values:", my_hashmap.values())
print("Items:", my_hashmap.items())

# Accessing values by key
print("Name:", my_hashmap.get("name"))
print("Gender:", my_hashmap.get("gender", "Not specified"))

# Removing a key-value pair
my_hashmap.remove("age")

print("Keys after removing 'age':", my_hashmap.keys())

```
## Map

Вам необходимо реализовать `SimpleMap` на языке Python, включая основные методы для манипуляции данными внутри `SimpleMap`. Ваша цель - создать класс Python с именем `SimpleMap`:

```python

class SimpleMap:
    def __init__(self):
        self.items = []

    def set(self, key, value):

    def get(self, key, default=None):

    def remove(self, key):

    def keys(self):


    def values(self):


    def items(self):



# Example usage:
my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
```

# Work In Progress
# Балльные задания

## Односвязный список — замена узлов

```c
list1 = linked_list(1 -> 2 -> 3 -> 4)
list2 = linked_list(5 -> 6 -> 7 -> 8)

swap_node(&list1, 2, &list2, 0)
>> true

print(list1)
>> linked_list(1 -> 2 -> 5 -> 4)
print(list2)
>> linked_list(3 -> 6 -> 7 -> 8)
```

```c
list1 = linked_list(1 -> 2 -> 3)
list2 = linked_list(4 -> 5 -> 6)

swap_node(&list1, 1, &list2, 3)
>> false  // (index 3 of list2 does not exist)

print(list1)
>> linked_list(1 -> 2 -> 3)
print(list2)
>> linked_list(4 -> 5 -> 6)
```

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

	def linked_list(*values):
	
	def print_linked_list(linked_list):
	
	def swap_nodes(list_pointer1, index1, list_pointer2, index2):
	
	    return True
	
	def get_node_and_prev(linked_list, index):


# Example usage
list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  # Output: True

print_linked_list(list1)
# Output: 1 -> 2 -> 5 -> 4 -> None

print_linked_list(list2)
# Output: 3 -> 6 -> 7 -> 8 -> None

list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  # Output: False

print_linked_list(list1)
# Output: 1 -> 2 -> 3 -> None

print_linked_list(list2)
# Output: 4 -> 5 -> 6 -> None
```


## Развлекаемся со списками: уменьшаем

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reduce(head, func, initial_value):
    current = head
    accumulator = initial_value


    return accumulator

def add(acc, curr):
    return acc + curr

list1 = Node(1, Node(2, Node(3)))
result1 = reduce(list1, add, 0)
print(result1)  # Output: 6

def multiply(acc, curr):
    return acc * curr

list2 = Node(1, Node(2, Node(3, Node(4))))
result2 = reduce(list2, multiply, 1)
print(result2)  # Output: 24

```

## Развлекаемся со списками : получить N-й

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(head, index):
    if head is None or index < 0:
        raise ValueError("Invalid index or empty list")
        
    return current


list1 = Node(1, Node(2, Node(3)))
result1 = get_nth(list1, 0)
print(result1.data)  # Output: 1


list2 = Node(1, Node(2, Node(3, None)))
result2 = get_nth(list2, 2)
print(result2.data)  # Output: 3

try:
    get_nth(list2, 5)
except ValueError as e:
    print(e)  # Output: Index out of range

try:
    get_nth(None, 0)
except ValueError as e:
    print(e)  # Output: Invalid index or empty list
```

## Связанные списки — длина и количество

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(head):
    count = 0
    return count

def count(head, value):
    count = 0
    return count


list1 = Node(1, Node(2, Node(3)))
result_length = length(list1)
print(result_length)  # Output: 3


result_count = count(list1, 1)
print(result_count)  # Output: 1


list2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3)))))))))
result_count_2 = count(list2, 2)
print(result_count_2)  # Output: 4

```

## IPv4 to int32

```python
def ip_to_int32(ip):
   
    return result

ip_address = "128.32.10.1"
result = ip_to_int32(ip_address)
print(result)  # Output: 2149583361

```

## Подсчитайте IP-адреса

```python
def ips_between(start, end):
    return result

def ip_to_int32(ip):

    return int(binary_representation, 2)

result1 = ips_between("10.0.0.0", "10.0.0.50")
print(result1)  # Output: 50

result2 = ips_between("10.0.0.0", "10.0.1.0")
print(result2)  # Output: 256

result3 = ips_between("20.0.0.10", "20.0.1.0")
print(result3)  # Output: 246

```

## Умножение квадратной матрицы

```python
def matrix_mult(a, b):
    return result

matrix_a = [[1, 2], [3, 2]]
matrix_b = [[3, 2], [1, 1]]

result_matrix = matrix_mult(matrix_a, matrix_b)
print(result_matrix)
# Output: [[5, 4], [11, 8]]
```

## Улитка

```python
def snail(array):

    return result

array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = snail(array1)
print(result1)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

array2 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
result2 = snail(array2)
print(result2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## Развлечение со списками: карта

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def map_linked_list(head, mapping_function):
    
    return new_head

# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a mapping function: x => x * 2
def mapping_function(x):
    return x * 2

# Apply the map method
mapped_list = map_linked_list(original_list, mapping_function)

# Print the result
current = mapped_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 4 -> 6 ->

```

## Развлечение со списками: фильтр

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def filter_linked_list(head, predicate_function):
    current = head
    new_head = None
    new_current = None

    return new_head


# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a predicate function: x => x >= 2
def predicate_function(x):
    return x >= 2

# Apply the filter method
filtered_list = filter_linked_list(original_list, predicate_function)

# Print the result
current = filtered_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 3 ->

```

## Развлечение со списками: AnyMatch + allMatch

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def any_match(head, predicate_function):
    current = head

    return False

def all_match(head, predicate_function):
    current = head
    return True

# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a predicate function: x => x > 1
def predicate_function(x):
    return x > 1

# Apply the any_match method
result_any_match = any_match(original_list, predicate_function)
print(result_any_match)  # Output: True

# Apply the all_match method
result_all_match = all_match(original_list, predicate_function)
print(result_all_match)  # Output: False

```

## Развлечение со списками: LastIndexOf

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def last_index_of(head, value):
    current = head
    last_index = -1
    current_index = 0
    return last_index

# Define a linked list: 1 -> 2 -> 3 -> 3
original_list = Node(1, Node(2, Node(3, Node(3))))

# Find the last index of value 3
result = last_index_of(original_list, 3)
print(result)  # Output: 3

```

## Развлечение со списками: indexOf
```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def index_of(head, value):


# Define a linked list: 1 -> 2 -> 3 -> 3
original_list = Node(1, Node(2, Node(3, Node(3))))

# Find the index of value 3
result = index_of(original_list, 3)
print(result)  # Output: 2

```

## Развлечение со списками: countIf

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def count_if(head, predicate_function):


# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a predicate function: x => x >= 2
def predicate_function(x):
    return x >= 2

# Count the number of elements that satisfy the predicate
result = count_if(original_list, predicate_function)
print(result)  # Output: 2

```

## Удобочитаемый формат продолжительности

```python
def format_duration(seconds):

# Example usage
print(format_duration(62))    # Output: "1 minute and 2 seconds"
print(format_duration(3662))  # Output: "1 hour, 1 minute and 2 seconds"
```

## Убийственная гаражная дверь

```python
def controller(input_str):

# Example usage
input_str = '..P...O.....'
output_str = controller(input_str)
print(output_str)  # Output: "001234321000"
```