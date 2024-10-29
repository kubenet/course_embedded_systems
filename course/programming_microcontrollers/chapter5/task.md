# Курс: Программирование микроконтроллеров
## Практическое занятие №5. "HAL"

> Решение необходимо выложить на свой `github`

Изучить документацию на [`stm32l031k6`](https://www.st.com/en/microcontrollers-microprocessors/stm32l031k6.html#documentation) или [`stm32c031c6`](https://www.st.com/en/microcontrollers-microprocessors/stm32c031c6.html) и использование [stm32cube](https://www.st.com/en/development-tools/stm32cubemx.html) [libopencm3](https://libopencm3.org/) и [cmsis](https://arm-software.github.io/CMSIS_5/General/html/index.html) для разработки под данные мк.

Можете воспользоваться данными репозиториями для начала работы 
- [STM32 Nucleo64 C031C6 with STM32 HAL](https://github.com/wokwi/stm32-hello-wokwi)
- [CMSIS on STM32C031C6](https://github.com/WelsTheory/stm32_hello_cmsis_wokwi)
- [STM32 Nucleo32 l031k6 with STM32 HAL](https://github.com/savaleriy/stm32cube-hal-wokwi)
- [STM32 Nucleo32 l031k6 with libopencm3](https://github.com/savaleriy/stm32-libopencm3-wokwi)
- [STM32 Nucleo32 l031k6 with CMSIS](https://github.com/savaleriy/stm32-cmsis-wokwi)

### GPIO 

1. Hello world 
2. Реализовать обработчик нажатия кнопки, который будет отслеживать её состояние (нажата/отпущена). При нажатии кнопки должна включаться встроенная светодиодная индикация (например, мигание светодиода).

## Полезные материалы 
- [Библиотека libopencm3: Быстрый старт (Часть 1)](https://habr.com/ru/companies/auriga/articles/728270/)
- [Начинаем работать в STM32CubeMX. Часть 1](https://habr.com/ru/articles/310742/)
- [STM32 + CMSIS + STM32CubeIDE](https://habr.com/ru/articles/481478/)