# Вспомнить все

## Синтаксис C++

Первая программа 
```c++
#include <iostream>  
  
int main()  
{  
	std::cout << "Hello, World!";
}
```

### The main function[​](https://cpp-lang.net/learn/course/basics/first-program/#the-main-function "Direct link to The main function")

Каждая программа на C++ содержит фрагмент кода, который мы называем _главной функцией_. Это первый[1](https://cpp-lang.net/learn/course/basics/first-program/#user-content-fn-1) код, который запускается при старте программы.

```
int main(){}
```

Первая строка приведенного выше кода начинает **определение функции**. Оно состоит из возвращаемого типа `int`, имени `main` и параметров внутри `()` (в нашем случае их нет). Хотя большинство из этих терминов сейчас не важны, все, на что вам следует обратить внимание, это имя `main`. Ваша программа всегда должна содержать функцию `main`, заданную в этом формате.

Есть и другие варианты

Существует множество вариантов написания функции `main`, но пока мы остановимся на самом простом - том, который мы показали выше. Иногда можно встретить функцию `main`, которая начинается с одного из следующих вариантов:

```
int main(int argc, char* argv[])
```

```
int main(int argc, char** argv)
```

```
auto main(int argc, char** argv) -> int
```

```
auto main() -> int
```

Хотя вариантов может быть еще больше, все они делают одно и то же - определяют точку входа в программу. Мы рассмотрим различия между ними в дальнейшем.

#### Blocks of code[​](https://cpp-lang.net/learn/course/basics/first-program/#blocks-of-code "Direct link to Blocks of code")

Программе важно знать, где начинается и заканчивается `main`. Для этого мы используем блоки кода. Блок **кода** в C++ - это набор инструкций, заключенных в фигурные скобки:

Содержание блока кода
```
outside
int main(){
	inside
}
outside
```

Все, что находится между фигурными скобками, считается внутри блока кода, а все остальное - за его пределами.

#### Order of execution[​](https://cpp-lang.net/learn/course/basics/first-program/#order-of-execution "Direct link to Order of execution")

Функция `main` представляет собой блок кода, содержащий инструкции, предоставленные программистом. Компьютер выполняет инструкции по порядку, или, проще говоря, строка за строкой, сверху вниз. При запуске программы выполняется первая строка внутри `main`, затем вторая и так далее.

> REMEMBER
The content of the `main` function the first code run by the program.

In the following example, we put three instructions inside the `main` function to illustrate the order of execution. You'll learn more about the `std::cout` later in this lesson.

Step1 of 3

Preview of the execution order

```
#include <iostream>int main(){  std::cout << "This is an instruction that displays text.";  std::cout << "And this is another instruction that displays text.";  std::cout << "This is the third instruction that displays text.";}
```

### The `iostream` header file[​](https://cpp-lang.net/learn/course/basics/first-program/#the-iostream-header-file "Direct link to the-iostream-header-file")

![Illustration on header file inclusion](https://cpp-lang.net/img/tutorials/course/basic/first-program/include-iostream-en.webp)

What does the #include directive actually do :)  

At the very beginning of the code there is a line:

```
#include <iostream>
```

This allows us to use the standard input and output tools provided by C++. The name `iostream` is short for _input/output stream_. In practice this will let the us output text that the user can see and take input text to change what the program does.

The name `iostream` refers to a **header file** on your disk that comes with the _C++ standard library_. We will explain more about them and `#include` in near future. For now, remember that in most cases we put `#include <header_file>` at the beginning of the file.