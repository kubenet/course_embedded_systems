# Курс: Программирование микроконтроллеров
# Лабораторная работа №3. 

### Цель:

Создать устройство, способное анализировать звуковой сигнал музыки и визуализировать его в виде цветных эффектов на светодиодной RGB ленте. Использовать Arduino для управления анализом звука и управления светодиодной лентой для создания красочных эффектов в соответствии с музыкальными ритмами.

### Необходимые компоненты:

1. Arduino (любая модель)
2. Микрофонный модуль (или аналог)
3. Аналогово-цифровой преобразователь (ADC) для обработки аудиосигнала
4. Светодиодная RGB лента
5. Усилитель для звука (опционально)
6. Блок питания для светодиодной ленты
7. Резисторы и соединительные провода

### Задачи:

1. Подключить микрофонный модуль и ADC к Arduino для получения аудиосигнала.
2. Разработать программу для анализа аудиосигнала и определения частотного спектра.
3. Использовать полученные данные для управления светодиодной RGB лентой.
4. Создать визуальные эффекты, соответствующие частотам и амплитудам звукового сигнала.
5. Добавить настройки для кастомизации визуализации (цвета, яркость, реакция на разные частоты).
6. Реализовать синхронизацию визуализации с ритмами музыки.

```C++
#include <Tone.h>
//https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/
  

int notes[] = { 
NOTE_A3,
NOTE_B3,
NOTE_C4,
NOTE_D4,
NOTE_E4,
NOTE_F4,
NOTE_G4 };
  

// You can declare the tones as an array

Tone notePlayer[2];

void setup(void)
{
Serial.begin(9600);
notePlayer[0].begin(11);
notePlayer[1].begin(12);
}

void loop(void)
{
	char c;  
	if(Serial.available())
	{
		c = Serial.read();
		switch(c)
		{
			case 'a'...'g':
				notePlayer[0].play(notes[c - 'a']);
				int sensorValue = analogRead(11);
				Serial.print("Analog Value: ");
				Serial.println(sensorValue);
				Serial.print("Note Value: ");
				Serial.println(notes[c - 'a']);
				break;
			case 's':
				notePlayer[0].stop();
				break; 
			case 'A'...'G':
				notePlayer[1].play(notes[c - 'A']);
				int sensorValueUpper = analogRead(11);
				Serial.print("Analog Value (Upper): ");
				Serial.println(sensorValueUpper);
				Serial.print("Note Value: ");
				Serial.println(notes[c - 'A']);
				break;
			case 'S':
				notePlayer[1].stop();
				break;  
			default:
				notePlayer[1].stop();
				notePlayer[0].play(NOTE_B2);
				delay(300);
				notePlayer[0].stop();
				delay(100);
				notePlayer[1].play(NOTE_B2);
				delay(300);
				notePlayer[1].stop();
			break;
		}
	}
}
```


