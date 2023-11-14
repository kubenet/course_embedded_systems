# Курс: Программирование микроконтроллеров
# Практическое занятие №5. "Память"

# 1. **Определение Размера Структур в EEPROM:**
    
- **Описание:** Необходимо реализовать несколько структур данных с различными типами переменных (int, float, char) и различными размерами. Затем они должны сохранить эти структуры в EEPROM Arduino и измерить размер каждой структуры в байтах.
    - **Требования:**
        - Использование EEPROM для сохранения данных.
        - Измерение размера каждой структуры.

```c++
#include <EEPROM.h>

struct SensorData {
  int sensorValue;
  float temperature;
  char status;
};

void setup() {
  Serial.begin(9600);

  EEPROM.begin(512);

  SensorData data;
  int dataSize = sizeof(data);

  Serial.print("Size of SensorData: ");
  Serial.println(dataSize);
}

void loop() {
}
```
# 2. **Хранение Данных от Сенсора в EEPROM:**
    
- **Описание:** Необходимо реализовать программу для считывания данных с сенсора (например, температурного датчика) и сохранения их в EEPROM. Затем они должны реализовать функциональность для извлечения сохраненных данных и их отображения.
 - **Требования:**
        - Использование сенсора для получения данных.
        - Запись и чтение данных в/из EEPROM.

```c++
#include <EEPROM.h>

const int sensorPin = A0;
int currentAddress = 0;

struct SensorData {
  int sensorValue;
  unsigned long timestamp;
};

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);

  // Сохранение данных в EEPROM
  SensorData data;
  data.sensorValue = sensorValue;
  data.timestamp = millis();
  EEPROM.put(currentAddress, data);
  currentAddress += sizeof(SensorData);

  // Если достигнут конец EEPROM, начнем сначала
  if (currentAddress + sizeof(SensorData) > EEPROM.length()) {
    currentAddress = 0;
  }

  delay(1000);
}

void printDataFromEEPROM() {
  // Чтение данных из EEPROM и вывод на Serial
  int totalData = EEPROM.length() / sizeof(SensorData);
  for (int i = 0; i < totalData; ++i) {
    SensorData data;
    EEPROM.get(i * sizeof(SensorData), data);
    Serial.print("Sensor Value: ");
    Serial.print(data.sensorValue);
    Serial.print(", Timestamp: ");
    Serial.println(data.timestamp);
  }
}

```
# 3. **Шифрование и Защита Данных:**
    
- **Описание:** Необходимо реализовать программу для записи конфиденциальной информации (например, пароля) в EEPROM. Затем они должны реализовать механизм шифрования и дешифрования данных при сохранении и извлечении из EEPROM.
 - **Требования:**
	- Шифрование данных перед сохранением.
	- Дешифрование данных при извлечении.

```c++
#include <EEPROM.h>

void caesarEncryptDecrypt(char *data, int length, int shift) {
  for (int i = 0; i < length; ++i) {
    data[i] = data[i] + shift;
  }
}

void genericEncryptDecrypt(char *data, int length, int key, void (*encryptionFunction)(char*, int, int)) {
  encryptionFunction(data, length, key);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  char password[20]; // Пароль может быть длиной до 20 символов
  int shift = 3;
  int encryptedShift = shift;

  Serial.print("Enter password: ");
  while (!Serial.available()) {
    // Ожидание ввода пользователя
  }
  Serial.readBytesUntil('\n', password, sizeof(password));
  
  Serial.print("Enter encryption shift: ");
  while (!Serial.available()) {
    // Ожидание ввода пользователя
  }
  encryptedShift = Serial.parseInt();
  Serial.println(encryptedShift);

  genericEncryptDecrypt(password, sizeof(password), encryptedShift, caesarEncryptDecrypt);
  for (int i = 0; i < sizeof(password); ++i) {
    EEPROM.write(i, password[i]);
  }

  Serial.println("Password encrypted and saved to EEPROM.");

  // Дешифрование из EEPROM
  for (int i = 0; i < sizeof(password); ++i) {
    password[i] = EEPROM.read(i);
  }
  genericEncryptDecrypt(password, sizeof(password), -encryptedShift, caesarEncryptDecrypt);

  Serial.print("Decrypted Password from EEPROM: ");
  Serial.println(password);

  delay(1000);
}
```
# 4. **Оптимизация Хранения Больших Данных:**

 - **Описание:** Необходимо реализовать работату с большим объемом данных, например, серией измерений с сенсора. Задача - разработать механизм оптимизации хранения этих данных в EEPROM, чтобы максимально эффективно использовать пространство памяти.
- **Требования:**
	- Оптимизировать структуры данных для хранения большого объема информации.
	- Измерить и сравнить эффективность использования памяти.

```c++
#include <EEPROM.h>

const int sensorPin = A0;
int currentAddress = 0;

struct SensorData {
  int sensorValue;
  unsigned long timestamp;
};

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);

  // Сохранение данных в EEPROM
  SensorData data;
  data.sensorValue = sensorValue;
  data.timestamp = millis();
  EEPROM.put(currentAddress, data);
  currentAddress += sizeof(SensorData);

  // Если достигнут конец EEPROM, начнем сначала
  if (currentAddress + sizeof(SensorData) > EEPROM.length()) {
    currentAddress = 0;
  }

  delay(1000);
}

void printDataFromEEPROM() {
  // Чтение данных из EEPROM и вывод на Serial
  int totalData = EEPROM.length() / sizeof(SensorData);
  for (int i = 0; i < totalData; ++i) {
    SensorData data;
    EEPROM.get(i * sizeof(SensorData), data);
    Serial.print("Sensor Value: ");
    Serial.print(data.sensorValue);
    Serial.print(", Timestamp: ");
    Serial.println(data.timestamp);
  }
}
```
# 5. **Создание Лога Событий с Использованием EEPROM:**
    
- **Описание:** Необходимо реализовать  систему логирования событий, используя датчики и сохраняя записи в EEPROM. Это может включать в себя временные метки, типы событий и другую связанную информацию. Студенты также должны создать механизм для вывода лога на экран или другой устройство.
- 
- **Требования:**
	- Использование различных датчиков для сбора данных.
	- Сохранение лога в EEPROM.
	- Вывод лога событий.

```c++
#include <EEPROM.h>

enum SensorState {
  IDLE,
  MEASURING,
  LOGGING
};

struct EventLog {
  unsigned long timestamp;
  char eventType;
  int sensorValue;
};

const int LOG_SIZE_LIMIT = 10; // Максимальный размер лога событий

SensorState currentState = IDLE;
unsigned long lastMeasurementTime = 0;

void logEvent(char eventType, int sensorValue) {
  int logSize = EEPROM.read(0);

  // Проверка на переполнение лога
  if (logSize >= LOG_SIZE_LIMIT) {
    Serial.println("Log full. Resetting log.");
    logSize = 0;
  }

  EventLog event;
  event.timestamp = millis();
  event.eventType = eventType;
  event.sensorValue = sensorValue;

  // Сохранение лога в EEPROM
  int address = sizeof(int) + logSize * sizeof(EventLog);
  EEPROM.put(address, event);
  EEPROM.write(0, logSize + 1);
}

void setup() {
  Serial.begin(9600);
  EEPROM.write(0, sizeof(int)); // Инициализация размера лога
}

void loop() {
  int sensorValue = analogRead(A0);

  switch (currentState) {
    case IDLE:
      currentState = MEASURING;
      lastMeasurementTime = millis();
      break;

    case MEASURING:
      if (millis() - lastMeasurementTime >= 1000) {
        currentState = LOGGING;
      }
      break;

    case LOGGING:
      logEvent('T', sensorValue);
      currentState = MEASURING;
      lastMeasurementTime = millis();
      break;
  }

  // Вывод лога каждые 3 секунды
  if (millis() % 3000 == 0) {
    Serial.println("Event Log:");
    int logSize = EEPROM.read(0);
    for (int i = 0; i < logSize; ++i) {
      EventLog event;
      EEPROM.get(sizeof(int) + i * sizeof(EventLog), event);
      Serial.print("Timestamp: ");
      Serial.print(event.timestamp);
      Serial.print(", Type: ");
      Serial.print(event.eventType);
      Serial.print(", Value: ");
      Serial.println(event.sensorValue);
    }
    Serial.println("End of Log");
  }

  delay(1000);
}

```