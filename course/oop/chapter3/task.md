# Курс: ООП
#oop #task
### Тема 1: Глубокое и поверхностное копирование

**Задание:** Изучить и реализовать концепции глубокого и поверхностного копирования на примере класса `Car`.

```c++
#include <iostream>
#include <cstring>

class Car {
private:
    char *make;
    char *model;
    int year;
    double mileage;

public:
    // Конструктор
    Car(const char *make, const char *model, int year, double mileage)
        : year(year), mileage(mileage) {
        this->make = new char[strlen(make) + 1];
        strcpy(this->make, make);
        this->model = new char[strlen(model) + 1];
        strcpy(this->model, model);
    }

    // Конструктор копирования (глубокое копирование)
    Car(const Car &other)
        : year(other.year), mileage(other.mileage) {
        make = new char[strlen(other.make) + 1];
        strcpy(make, other.make);
        model = new char[strlen(other.model) + 1];
        strcpy(model, other.model);
    }

    // Деструктор
    ~Car() {
        delete[] make;
        delete[] model;
        std::cout << "Car object has been destroyed." << std::endl;
    }

    // Метод вывода информации
    void displayInfo() const {
        std::cout << "Car: " << make << " " << model << " (" << year << "), Mileage: " << mileage << std::endl;
    }
};

// Основная функция
int main() {
    Car car1("Toyota", "Camry", 2020, 15000);
    Car car2 = car1;  // Вызов конструктора копирования
    car2.displayInfo();
    return 0;
}

```
### Тема 2: Наследование, композиция, агрегация, ассоциация, зависимость

**Задание:** Изучить и реализовать концепции наследования, композиции, агрегации, ассоциации и зависимости.
#### План работ для каждого задания:

1. **Композиция: Классы `Library` и `Book` и `Textbook`:**
    - Создать класс `Library`, который содержит массив объектов `Book` и `Textbook`.
    - Реализовать методы добавления и вывода информации о книгах в библиотеке.
        - `addBook(Book book)` – добавляет книгу в библиотеку.
        - `displayBooks()` – выводит список всех книг в библиотеке.
1. **Агрегация: Классы `Course` и `Student` и `InternationalStudent`:**
    - Создать класс `Course`, который содержит список студентов (использовать указатели).
    - Реализовать методы для добавления и вывода студентов в курсе.
2. **Ассоциация: Классы `Teacher` и `Student` и `InternationalStudent`:**
    - Создать класс `Teacher`, который имеет ссылку на объект `Student`.
    - Реализовать метод, который позволяет учителю оценивать студента.
3. **Зависимость: Класс `EmailSender`:**
    Создайте класс `NotificationService`, который будет зависеть от класса `EmailService`.
	- **Класс `EmailService`:**
	    - **Методы:**
	        - `sendEmail(String recipient, String message)` – отправляет email.
	- **Класс `NotificationService`:**
	    - **Методы:**
	        - `notifyUser(String recipient, String message)` – использует `EmailService` для отправки уведомлений.
### Тема 3: Полиморфизм

1. Создать базовый класс `Animal` с методом `sound()`.
2. Создать производные классы `Dog` и `Cat`, переопределяющие метод `sound()`.
3. Создать массив указателей на `Animal` и заполнить его объектами `Dog` и `Cat`.
4. Вывести звуки, используя полиморфизм.