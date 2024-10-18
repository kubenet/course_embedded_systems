#oop 


> Умные указатели [тык](https://habr.com/ru/companies/piter/articles/706866/)и [тык]

**Данное задание выдается на неделю**.
## Пример

Создайте систему управления автосалоном, которая включает классы для автомобилей и автосалона, а также реализацию интерфейсов для обслуживания и характеристик автомобилей. Реализуйте следующие функциональные возможности:

1. **Классы:**
    - **Car**: базовый шаблонный класс для автомобилей, содержащий информацию о марке, модели, годе выпуска и цене. Реализуйте методы для отображения информации об автомобиле и расчета скидки.
    - **ElectricCar** и **GasCar**: производные классы от `Car`, представляющие электрические и бензиновые автомобили соответственно. Реализуйте специфические методы для расчета дальности поездки, а также переопределите метод для отображения информации об автомобиле.
2. **Шаблонные классы и полиморфизм:**
    - Используйте шаблонный класс `Car`, чтобы поддерживать различные типы данных для цены (например, целые числа или числа с плавающей запятой). Реализуйте полиморфизм через виртуальные методы для отображения информации и расчета скидок.
    
3. **Интерфейсы:**
    
    - **IServiceable**: интерфейс, который определяет метод `Service()` для обслуживания автомобилей. Реализуйте этот интерфейс в классах `ElectricCar` и `GasCar`, добавив соответствующие действия (например, зарядка батареи для электрических автомобилей и заправка для бензиновых).
    - **ICarFeatures**: интерфейс, который определяет метод `CalculateRange()` для расчета дальности поездки автомобилей. Реализуйте этот интерфейс в классах `ElectricCar` и `GasCar`.
4. **Множественное наследование:**
    
    - Используйте множественное наследование, чтобы классы `ElectricCar` и `GasCar` наследовали функциональность как от базового класса `Car`, так и от интерфейсов `IServiceable` и `ICarFeatures`.
5. **Композиция и инкапсуляция:**
    
    - Создайте класс `Showroom`, который будет управлять списком автомобилей. Реализуйте методы для добавления автомобилей, отображения информации о всех автомобилях, расчета общей стоимости с учетом скидок и обслуживания всех автомобилей. Данные о автомобилях должны быть защищены и доступны через публичные методы.
6. **Случайная генерация объектов:**
    
    - Реализуйте функцию `CreateRandomCar()`, которая генерирует случайные объекты классов `ElectricCar` и `GasCar` с различными марками, моделями, годами выпуска и ценами. Используйте генератор случайных чисел для создания автомобилей.

### Ответ

```c++
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib> // Для rand() и srand()
#include <ctime>   // Для time()

// Интерфейс для обслуживания автомобилей
class IServiceable {
public:
    virtual void Service() = 0; // Метод для обслуживания
    virtual ~IServiceable() = default;
};

// Интерфейс для характеристик автомобилей
class ICarFeatures {
public:
    virtual double CalculateRange() const = 0; // Метод для расчета дальности поездки
    virtual ~ICarFeatures() = default;
};

// Определение шаблонного класса Car
template <typename T>
class Car {
protected:
    std::string make; // Марка автомобиля
    std::string model; // Модель автомобиля
    int year; // Год выпуска
    T price; // Цена автомобиля

public:
    Car(std::string m, std::string mod, int y, T p) : make(m), model(mod), year(y), price(p) {}
    
    virtual void DisplayInfo() const {
        std::cout << "Make: " << make << ", Model: " << model << ", Year: " << year << ", Price: $" << price << std::endl;
    }
    
    virtual T CalculateDiscount(double percentage) const {
        return price * (1 - percentage / 100);
    }

    virtual ~Car() = default; // Виртуальный деструктор
};

// Производный класс ElectricCar
template <typename T>
class ElectricCar : public Car<T>, public IServiceable, public ICarFeatures {
public:
    ElectricCar(std::string m, std::string mod, int y, T p) : Car<T>(m, mod, y, p) {}

    void DisplayInfo() const override {
        std::cout << "Electric Car - ";
        Car<T>::DisplayInfo();
    }

    void Service() override {
        std::cout << this->make << " " << this->model << " is being serviced (charging battery)." << std::endl;
    }

    double CalculateRange() const override {
        return 300.0; // Примерная дальность для электрического автомобиля
    }
};

// Производный класс GasCar
template <typename T>
class GasCar : public Car<T>, public IServiceable, public ICarFeatures {
public:
    GasCar(std::string m, std::string mod, int y, T p) : Car<T>(m, mod, y, p) {}

    void DisplayInfo() const override {
        std::cout << "Gas Car - ";
        Car<T>::DisplayInfo();
    }

    void Service() override {
        std::cout << this->make << " " << this->model << " is being serviced (refueling)." << std::endl;
    }

    double CalculateRange() const override {
        return 400.0; // Примерная дальность для бензинового автомобиля
    }
};

// Класс Showroom
class Showroom {
private:
    std::vector<Car<double>*> cars; // Список автомобилей

public:
    ~Showroom() {
        for (auto car : cars) {
            delete car; // Освобождение памяти
        }
    }

    void AddCar(Car<double>* car) {
        cars.push_back(car);
    }

    void DisplayAllCars() const {
        for (const auto& car : cars) {
            car->DisplayInfo();
        }
    }

    double CalculateTotalPrice(double discountPercentage) const {
        double total = 0.0;
        for (const auto& car : cars) {
            total += car->CalculateDiscount(discountPercentage);
        }
        return total;
    }

    void ServiceAllCars() const {
        for (const auto& car : cars) {
            if (IServiceable* serviceable = dynamic_cast<IServiceable*>(car)) {
                serviceable->Service();
            }
        }
    }
};

// Функция для генерации случайных автомобилей
Car<double>* CreateRandomCar() {
    std::string makes[] = {"Tesla", "Toyota", "Ford", "Nissan", "BMW"};
    std::string models[] = {"Model S", "Corolla", "Mustang", "Leaf", "X5"};
    int year = rand() % 21 + 2000; // Год от 2000 до 2020
    double price = (rand() % 40000 + 10000) + static_cast<double>(rand()) / RAND_MAX; // Цена от 10,000 до 50,000

    int type = rand() % 2; // 0 для электрических, 1 для бензиновых
    if (type == 0) {
        return new ElectricCar<double>(makes[rand() % 5], models[rand() % 5], year, price); // Электрические автомобили
    } else {
        return new GasCar<double>(makes[rand() % 5], models[rand() % 5], year, price); // Бензиновые автомобили
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0))); // Инициализация генератора случайных чисел
    Showroom showroom;

    // Генерация 10 случайных автомобилей
    for (int i = 0; i < 10; ++i) {
        Car<double>* car = CreateRandomCar();
        showroom.AddCar(car);
    }

    std::cout << "Cars in the showroom:" << std::endl;
    showroom.DisplayAllCars();

    double discountPercentage = 10.0; // Скидка 10%
    std::cout << "\nTotal price after " << discountPercentage << "% discount: $" 
              << showroom.CalculateTotalPrice(discountPercentage) << std::endl;

    std::cout << "\nServicing cars:" << std::endl;
    showroom.ServiceAllCars();

    return 0;
}

```


## Библиотека

**Описание задачи:**

Создайте систему управления библиотекой, которая включает классы для книг, пользователей и библиотеки. Реализуйте следующие функциональные возможности:
1. **Классы:**
    - **Book**: содержит информацию о книге (название, автор, ISBN, год издания, статус доступности). Реализуйте перегрузку оператора `<<` для удобного вывода информации о книге.
    - **User**: содержит информацию о пользователе (имя, уникальный ID, список взятых книг). Реализуйте методы для добавления и удаления книг из списка.
    - **Library**: содержит список книг и пользователей. Реализуйте методы для добавления книг и пользователей, поиска книг по различным критериям, выдачи книг пользователям и возврата книг.
2. **Наследование и полиморфизм:**
    - Создайте базовый класс `Item`, от которого будут наследоваться `Book` и, возможно, другие элементы (например, `Magazine`, `Journal`).
    - Реализуйте виртуальный метод для вывода информации о предметах.
3. **Композиты и инкапсуляция:**
    - В классе `Library` используйте композицию для хранения списков книг и пользователей. Все данные должны быть защищены, а доступ к ним — через публичные методы.
4. **Перегрузка методов:**
    - В классе `Library` перегрузите метод поиска книги: один вариант должен принимать название книги, другой — ISBN.
5. **Множественное наследование:**
    - Создайте интерфейс `Borrowable`, который будет иметь методы для взятия и возврата книг. Реализуйте этот интерфейс в классе `Book`.

### Шаблон

```c++
#include <iostream>

// Интерфейс Borrowable
class Borrowable {
};

// Базовый класс Item
class Item {
};

// Класс Book
class Book {
};

// Класс User
class User {
};

// Класс Library
class Library {
};

// Тестирование
int main() {
    Library library;
    
	// Пример проверки
	
    // Создание книг
    auto book1 = std::make_shared<Book>("1984", "George Orwell", "123456789", 1949);
    auto book2 = std::make_shared<Book>("To Kill a Mockingbird", "Harper Lee", "987654321", 1960);

    // Добавление книг в библиотеку
    library.addBook(book1);
    library.addBook(book2);

    // Создание пользователя
    auto user = std::make_shared<User>("Alice", 1);
    library.addUser(user);

    // Пользователь берет книгу
    user->addBook(book1);

    // Проверка информации о книгах
    book1->displayInfo();
    book2->displayInfo();

    // Возврат книги
    user->removeBook(book1);
    book1->displayInfo();

    return 0;
}
```
## Банк

Создайте систему управления банковскими счетами, которая включает классы для клиентов, банковских счетов и банка. Реализуйте следующие функциональные возможности:

1. **Классы:**
    - **Account**: базовый класс для банковского счета, который содержит информацию о счете (номер счета, баланс, тип счета). Реализуйте методы для пополнения и снятия средств.
    - **SavingsAccount** и **CheckingAccount**: производные классы от `Account`, которые добавляют специфические особенности (например, процент на сбережения для `SavingsAccount` и возможность овердрафта для `CheckingAccount`). Реализуйте перегрузку метода для вывода информации о счете.
    - **Customer**: класс, который содержит информацию о клиенте (имя, уникальный ID, список счетов). Реализуйте методы для добавления и удаления счетов из списка.
    - **Bank**: класс, который управляет клиентами и их счетами. Реализуйте методы для добавления клиентов, открытия и закрытия счетов, а также для выполнения операций перевода между счетами.
2. **Наследование и полиморфизм:**
    - Используйте полиморфизм для реализации общего метода `DisplayInfo()` в базовом классе `Account`, который будет переопределяться в производных классах.
3. **Композиты и инкапсуляция:**
    - В классе `Customer` используйте композицию для хранения списка счетов. Все данные должны быть защищены, а доступ к ним — через публичные методы.
4. **Перегрузка методов:**
    - В классе `Bank` перегрузите метод для получения информации о счетах: один вариант должен возвращать все счета клиента, другой — только счета с определенным балансом.
5. **Множественное наследование:**
    - Создайте интерфейс `Transactable`, который будет иметь методы для выполнения операций пополнения и снятия. Реализуйте этот интерфейс в классе `Account`.

### Шаблон

```c++
#include <iostream>

// Интерфейс для транзакций
class Transactable {
};

// Базовый класс для банковского счета
class Account : public Transactable {
};

// Класс для сберегательного счета
class SavingsAccount : public Account {
};

// Класс для расчетного счета
class CheckingAccount : public Account {
};

// Класс для клиента
class Customer {
};

// Класс для банка
class Bank {

};

int main() {

	// Пример проверки 
    Bank bank;

    auto customer1 = make_shared<Customer>("Иван Иванов", "001");
    bank.addCustomer(customer1);

    auto savingsAccount = make_shared<SavingsAccount>("12345", 1000.0, 0.05);
    customer1->addAccount(savingsAccount);

    auto checkingAccount = make_shared<CheckingAccount>("67890", 500.0, 200.0);
    customer1->addAccount(checkingAccount);

    // Демонстрация работы методов deposit и withdraw
    cout << "Перед пополнением и снятием:" << endl;
    bank.displayCustomerAccounts("001");

    savingsAccount->deposit(200.0);
    checkingAccount->withdraw(100.0);

    cout << "\nПосле пополнения и снятия:" << endl;
    bank.displayCustomerAccounts("001");

    // Попытка снять больше, чем доступно
    checkingAccount->withdraw(700.0);

    cout << "\nПосле попытки превышения лимита:" << endl;
    bank.displayCustomerAccounts("001");

    return 0;
}

```

## Зоопарк 

Создайте систему управления зоопарком, которая включает классы для животных и зоопарка. Реализуйте следующие функциональные возможности:

1. **Классы:**
    - **Animal**: базовый шаблонный класс для животных, который содержит информацию о животном (имя, возраст, вес). Реализуйте виртуальные методы для издания звуков и отображения информации о животном.
    - **Mammal** и **Bird**: производные классы от `Animal`, которые представляют млекопитающих и птиц соответственно. Реализуйте специфические звуки для каждого типа животных и переопределите метод для отображения информации.
    - **IFeedable**: интерфейс, который определяет метод `Feed()` для кормления животных. Реализуйте этот интерфейс в классах `Mammal` и `Bird`.
    - **Zoo**: класс, который управляет списком животных. Реализуйте методы для добавления животных, отображения информации о всех животных, издания звуков и кормления всех животных.
2. **Шаблонные классы и полиморфизм:**
    - Используйте шаблонный класс `Animal`, чтобы поддерживать различные типы данных для веса животных (например, целые числа или числа с плавающей запятой). Реализуйте полиморфизм через виртуальные методы для отображения информации и издания звуков.
3. **Композиция и инкапсуляция:**
    - В классе `Zoo` используйте композицию для хранения списка животных. Все данные о животных должны быть защищены, а доступ к ним — через публичные методы.
4. **Случайная генерация объектов:**
    - Реализуйте функцию `CreateRandomAnimal()`, которая будет генерировать случайные объекты классов `Mammal` и `Bird` с различными именами, возрастом и весом. Используйте генератор случайных чисел для создания животных.
5. **Интерфейсы и наследование:**
    - Создайте интерфейс `IFeedable` для реализации кормления животных. Убедитесь, что классы `Mammal` и `Bird` реализуют этот интерфейс.
### Шаблон 

```c++
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib> // Для rand() и srand()
#include <ctime>   // Для time()

// Интерфейс для кормления животных
class IFeedable {
};

// Определение шаблонного класса Animal
template <typename T>
class Animal {
};

// Производный класс Mammal
template <typename T>
class Mammal{
};

// Производный класс Bird
template <typename T>
};

// Класс Zoo
class Zoo {
};

// Функция для генерации случайных животных
Animal<double>* CreateRandomAnimal() {
    std::string names[] = {"Lion", "Tiger", "Elephant", "Parrot", "Eagle"};
    int age = rand() % 15 + 1; // Возраст от 1 до 15
    double weight = (rand() % 200 + 50) + static_cast<double>(rand()) / RAND_MAX; // Вес от 50 до 250

    int type = rand() % 2; // 0 для млекопитающих, 1 для птиц
    if (type == 0) {
        return new Mammal<double>(names[rand() % 3], age, weight); // Млекопитающие
    } else {
        return new Bird<double>(names[rand() % 2 + 3], age, weight); // Птицы
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0))); // Инициализация генератора случайных чисел
    Zoo zoo;

    // Генерация 10 случайных животных
    for (int i = 0; i < 10; ++i) {
        Animal<double>* animal = CreateRandomAnimal();
        zoo.AddAnimal(animal);
    }

    std::cout << "Animals in the zoo:" << std::endl;
    zoo.DisplayAllAnimals();

    std::cout << "\nAnimals making sounds:" << std::endl;
    zoo.MakeSounds();

    std::cout << "\nFeeding animals:" << std::endl;
    zoo.FeedAllAnimals();

    return 0;
}
```