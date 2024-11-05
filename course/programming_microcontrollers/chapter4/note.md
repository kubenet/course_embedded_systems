# Курс: Программирование микроконтроллеров
## Практическое занятие №4. "SPI и TFT Дисплеи"

## SPI

Последовательный периферийный интерфейс (Serial Peripheral Interface, `SPI`) — еще одна последовательная шина для подключения периферийных устройств к плате Arduino. Это быстрая шина, но для передачи данных в ней используются четыре линии против двух, используемых интерфейсом `I2C`. В действительности `SPI` не является истинной шиной, так как четвертая линия в нем называется «выбор ведомого» (`Slave  Select, SS`). Каждое периферийное устройство на шине должно быть соединено своей линией `SS` с отдельным контактом на плате `Arduino`. Такая схема подключения эффективно выбирает нужное периферийное устройство на шине, отключая все остальные.

Интерфейс `SPI` поддерживается широким спектром устройств, включая многие типы тех же устройств, что поддерживают `I2C`. Нередко периферийные устройства поддерживают оба интерфейса, `I2C` и `SPI`.

Линии тактового сигнала системы (`System  Clock, SCLK`), выход ведущего/ вход ведомого (`Master  Out  Slave  In, MOSI`) и вход ведущего/выход ведомого (`Master  In  Slave  Out, MISO`) подключаются к контактам на плате Arduino с теми же именами, которые в модели `Uno` соответствуют контактам `D13`, `D11` и `D12`. Линиями выбора ведомого могут быть любые контакты на плате `Arduino`. Они используются для выбора определенного ведомого устройства непосредственно перед передачей данных и его отключения по завершении обмена данными.

Ни к одной из линий не требуется подключать подтягивающее сопротивление.

## Дисплей 7735S

`TFT` дисплей - самые дешевые и распространенный тип дисплеев. `TFT` значит тонкопленочный транзистор, то есть способ создания этих дисплеев.

Данный дисплей может быть в двух исполнениях: синем и красном цвете. В зависимости от цвета, название выходов различается, но смысл остается тот же.

![](https://static.insales-cdn.com/images/products/1/3116/141265964/1396.jpg)

<![if !vml]>![](file:///C:\users\asvalera\Temp\msohtmlclip1\01\clip_image006.gif)<![endif]>

## Практика

Далее мы рассмотрим несколько интересных программ для наших дисплеев. Нам понадобятся библиотеки `SPI` и `TFT`. Их можно найти в менеджере библиотек(инструменты - управлять библиотеками), если в поисковой строке ввести `TFT`. Эта библиотека уже включает в себя все необходимое.

### Основные функции и вывод надписи на дисплей

Подключение необходимых библиотек
```arduino
#include <TFT.h>  // Библиотека для вывода графики

#include "SPI.h"  // Подключить библиотеку для работы с интерфейсом SPI

TFT  TFTscreen = TFT(10, 9, 8); // Настроить выводы для работы с дисплеем
```
Теперь добавьте следующие строки в функцию `void  setup()`, чтобы настроить дисплей:
```arduino
TFTscreen.begin();  // Активировать дисплей

TFTscreen.background(0, 0, 0); // Очистить экран дисплея
```
В первую очередь нужно настроить цвет фона для будущего изображения. Делается

это так:

`TFTscreen.background(b, g, r); // Установить цвет фона`

Цвет фона задается в формате `RGB` — тремя числами, определяющими интенсивность трех базовых цветов (красного, зеленого, синего) в диапазоне от 0 до 255.

К примеру, белый фон можно получить, задав максимальную интенсивность всех трех цветов — `255, 255, 255`. Чистый красный фон — задав интенсивность базового красного цвета равной `255`, а синего и зеленого — `0`. Для черного фона интенсивность всех трех цветов должна быть равна нулю.

Дальше нужно задать размер текста, если вы собираетесь выводить его в первый раз или если нужно изменить размер в середине скетча:

`TFTscreen.setTextSize(x);`

где `x`  — число от 1 до 5, определяющее размер текста

Далее вызовом следующей функции определяется цвет текста:

`TFTscreen.stroke(B, G, R);`

где _B_, _G_  и _R_  — значения интенсивности базовых цветов: синего, зеленого и красного.

Теперь можно вывести на экран сам текст:

`TFTscreen.text("Hello, world!", x, y);`
Этот вызов функции выведет текст «Hello, world!», начиная с позиции _x_  и _y_  на экране дисплея.

### Вывод сопротивления потенциометра на экран
```arduino
#include <TFT.h>  
#include <SPI.h>  
  
_// pin definition for the Uno_  
#define cs  10  
#define dc  9  
#define rst  8  
  
TFT TFTscreen = TFT(cs, dc, rst);  
  
_// позиция линии, отображающеей сопротивление, на экране_  
int xPos = 0;  
  
void  setup() {  
Serial.begin(9600);  
  
_// инициализируем дисплей_  
TFTscreen.begin();  
  
_// создаем задний фон_  
TFTscreen.background(250, 16, 200);  
}  
  
void  loop() {  
_// считываем показания с потенциометра, и масштабируем его к высоте экрана_  
int sensor = analogRead(A0);  
int drawHeight = map(sensor, 0, 1023, 0, TFTscreen.height());  
  
Serial.println(drawHeight);  
  
_// рисуем линию_  
TFTscreen.stroke(250, 180, 10);  
TFTscreen.line(xPos, TFTscreen.height() - drawHeight, xPos, TFTscreen.height());  
  
_// если линия подходит к краю экрана - обновляем экран_  
if (xPos >= 160) {  
xPos = 0;  
TFTscreen.background(250, 16, 200);  
} else {_// инкрементируем горизонтальную позицию_  
xPos++;  
}  
delay(16);  
}
```
### Вывод показания датчика на экран

Для вывода значения числовой переменной придется приложить немного больше усилий. Ее нужно преобразовать в символьный массив, размер которого соответствует максимально возможному значению. Если переменная предназначена для хранения значения, прочитанного с аналогового входа 0, и вам нужно вывести ее значение на экран, используйте такое объявление символьного массива:

`char  analogZero[4];`

Далее в скетче перед выводом аналогового значения на экран дисплея преобразуйте значение в строку

`String sensorVal = String(analogRead(A0));`

Скопируйте содержимое этой строки в символьный массив:

`sensorVal.toCharArray(analogZero, 4);`

И наконец, выведите символьный массив на экран командой .text():

`TFTscreen.text(_analogZero, x, y_);`

которая выведет значение _analogZero_, начиная с позиции с координатами _x_, _y_.

**Пример с выводом показаний датчика на дисплей**
```arduino
#include  <TFT.h>  
#include  <SPI.h>  
  
#define  cs 10  
#define  dc 9  
#define  rst 8  
  
TFT  TFTscreen = TFT(cs, dc, rst);  
  
_// создадим массив для вывода на экран значений_  
char  sensorPrintout[4];  
  
void  setup() {  
  
_// инициализируем экран_  
TFTscreen.begin();  
  
_// ставим черный фон_  
TFTscreen.background(0, 0, 0);  
  
_// пишем текст на экран белого цвета_  
TFTscreen.stroke(255, 255, 255);  
_// задаем размер текста_  
TFTscreen.setTextSize(2);  
_// передвигаем курсор в левый верхний угол, чтобы начать писать оттуда_  
TFTscreen.text("Sensor  Value :\n ", 0, 0);  
_// задаем размер текста для значений с потенциометра_  
TFTscreen.setTextSize(5);  
}  
  
void  loop() {  
  
_// считываем значения с потенциометра в переменную типа_ _string_  
String  sensorVal = String(analogRead(A0));  
  
_// преобразуем полученную строку в массив символов_  
sensorVal.toCharArray(sensorPrintout, 4);  
  
TFTscreen.stroke(255, 255, 255);  
_// выводим значения на экран_  
TFTscreen.text(sensorPrintout, 0, 20);  
delay(250);  
TFTscreen.stroke(0, 0, 0);  
TFTscreen.text(sensorPrintout, 0, 20);  
}
```

### Цифровой термометр

Этот проект только кажется сложным — на деле он довольно прост в реализации и требует всего двух функций. Первая принимает показания с датчика температуры TMP36 и сохраняет в массиве со 120 значениями. Каждый раз после выполнения нового замера результаты предыдущих 119 смещаются в массиве вниз, чтобы освободить место для новых данных. Самые старые значения затираются следующими за ними.

Вторая функция создает изображение на экране дисплея. Ее задача — отобразить текущую температуру, определить масштаб для графика и вывести каждый замер в виде пикселя на экране для получения графика изменения температуры во времени.
```arduino
#include  <TFT.h> // Библиотека для работы с графическим дисплеем  
#include  <SPI.h> // Библиотека для работы с интерфейсом SPI  
TFT  TFTscreen = TFT(10, 9, 8); _// Назначить выводы цифровых сигналов_  
int  tcurrent = 0;  
int  tempArray[120];  
char  currentString[3];  
void  getTemp() _// Функция чтения температуры с датчика_ _TMP__36_  
{  
float  sum = 0;  
float  voltage = 0;  
float  sensor = 0;  
float  celsius;  
_// Прочитать значение с датчика и преобразовать_  
_// его в градусы Цельсия_  
sensor = analogRead(5);  
voltage = (sensor * 5000) / 1024;  
voltage = voltage - 500;  
celsius = voltage / 10;  
tcurrent = int(celsius);  
_// Вставить новый замер в начало массива_  
for (int  a = 119 ; a >= 0 ; --a )  
{tempArray[a] = tempArray[a - 1];  
}  
tempArray[0] = tcurrent;  
}  
  
void  drawScreen() _// Выводит изображение на экран ЖКИ_  
{  
int  q;  
_// Вывести текущую температуру_  
TFTscreen.background(0, 0, 0); _// Очистить экран, установив черный цвет фона_  
TFTscreen.stroke(255, 255, 255); _// Белый текст_  
TFTscreen.setTextSize(2);  
TFTscreen.text("Current:", 20, 0);  
String  tempString = String(tcurrent);  
tempString.toCharArray(currentString, 3);  
TFTscreen.text(currentString, 115, 0);  
_// Нарисовать оси графика_  
TFTscreen.setTextSize(1);  
TFTscreen.text("50", 0, 20);  
TFTscreen.text("45", 0, 30);  
TFTscreen.text("40", 0, 40);  
TFTscreen.text("35", 0, 50);  
TFTscreen.text("30", 0, 60);  
TFTscreen.text("25", 0, 70);  
TFTscreen.text("20", 0, 80);  
TFTscreen.text("15", 0, 90);  
TFTscreen.text("10", 0, 100);  
TFTscreen.text(" 5", 0, 110);  
TFTscreen.text(" 0", 0, 120);  
TFTscreen.line(20, 20, 20, 127);  
_// Нарисовать график изменения температуры_  
for (int  a = 25 ; a < 145 ; a++)  
{  
_// Преобразовать температуру в координату_ _Y_ _на экране ЖКИ_  
q = (123 - (tempArray[a - 25] * 2));  
TFTscreen.point(a, q);  
} }  
void  setup()  
{  
void  loop() {  
getTemp();  
drawScreen();  
for (int  a = 0 ; a < 20 ; a++) _// Ждать 20 минут до следующего замера_  
{  
delay(60000); _// Ждать 1 минуту_  
}  
}
```
### Игра Pong

Для игры нам понадобится подключить второй потенциометр, чтобы управлять платформой в двух направлениях.
```arduino
#include  <TFT.h>  // Arduino  LCD  library  
#include  <SPI.h>  
  
#define  cs 10  
#define  dc 9  
#define  rst 8  
  
TFT  TFTscreen = TFT(cs, dc, rst);  
  
_// переменные для значений положений платформы и шара_  
int  paddleX = 0;  
int  paddleY = 0;  
int  oldPaddleX, oldPaddleY;  
int  ballDirectionX = 1;  
int  ballDirectionY = 1;  
  
int  ballSpeed = 10; _// скорость шара - уменьшение этого значения делает его быстрее_  
  
int  ballX, ballY, oldBallX, oldBallY;  
  
void  setup() {  
TFTscreen.begin();  
TFTscreen.background(0, 0, 0);  
}  
  
void  loop() {  
  
_// сохраняем в переменные высоту и ширину экрана_  
int  myWidth = TFTscreen.width();  
int  myHeight = TFTscreen.height();  
  
_// масштабируем значения с потенциометров к размерам нашего экрана_  
paddleX = map(analogRead(A0), 512, -512, 0, myWidth) - 20 / 2;  
paddleY = map(analogRead(A1), 512, -512, 0, myHeight) - 5 / 2;  
  
TFTscreen.fill(0, 0, 0);  
  
if (oldPaddleX != paddleX || oldPaddleY != paddleY) {  
TFTscreen.rect(oldPaddleX, oldPaddleY, 20, 5);  
}  
  
_// рисуем платформу и сохраняем ее позицию_  
TFTscreen.fill(255, 255, 255);  
  
TFTscreen.rect(paddleX, paddleY, 20, 5);  
oldPaddleX = paddleX;  
oldPaddleY = paddleY;  
  
_// обновляем позицию шара_  
if (millis() % ballSpeed < 2) {  
moveBall();  
}  
}  
  
_// функция, регистрирующая положение шара на экране_  
void moveBall() {_// if the ball goes offscreen, reverse the direction:_  
if (ballX > TFTscreen.width() || ballX < 0) {  
ballDirectionX = -ballDirectionX;  
}  
  
if (ballY > TFTscreen.height() || ballY < 0) {  
ballDirectionY = -ballDirectionY;  
}  
  
if (inPaddle(ballX, ballY, paddleX, paddleY, 20, 5)) {  
ballDirectionX = -ballDirectionX;  
ballDirectionY = -ballDirectionY;  
}  
  
ballX += ballDirectionX;  
ballY += ballDirectionY;  
  
TFTscreen.fill(0, 0, 0);  
  
if (oldBallX != ballX || oldBallY != ballY) {  
TFTscreen.rect(oldBallX, oldBallY, 5, 5);  
}  
  
TFTscreen.fill(255, 255, 255);  
TFTscreen.rect(ballX, ballY, 5, 5);  
  
oldBallX = ballX;  
oldBallY = ballY;  
  
}  
  
boolean inPaddle(int x, int y, int rectX, int rectY, int rectWidth, int rectHeight) {boolean result = false;if ((x >= rectX && x <= (rectX + rectWidth)) &&  
(y >= rectY && y <= (rectY + rectHeight))) {  
result = true;  
}return result;  
}
```

## Дополнительные материалы

[Подробнее про функции библиотеки TFT](https://wikihandbk.com/wiki/Arduino:%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8/TFT)
[Большая статья на Амперке, посвященная библиотеке UTFT](http://wiki.amperka.ru/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B:tft-lcd-240x320) 
[LCDWIKI3](http://www.lcdwiki.com/1.44inch_SPI_Module_ST7735S_SKU:MSP1443) 
[Документация](https://docs.wokwi.com/parts/wokwi-ili9341)
[Пример](https://wokwi.com/projects/377635992487870465)

----

