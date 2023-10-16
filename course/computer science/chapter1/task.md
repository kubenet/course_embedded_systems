# Инофрматика

## Введение в двоичную систему
    
1.  Преобразовать десятичное число 13 в двоичное число.
2.  Преобразовать десятичное число 45 в двоичное число.
3.  Преобразовать десятичное число 100 в двоичное число.
4.  Сложить двоичные числа 1011 и 1101.
5.  Сложить двоичные числа 101010 и 110110.
6.  Вычесть двоичное число 11001 из числа 101010.
7.  Вычесть двоичное число 10110 из числа 110010.
8.  Умножить двоичные числа 101 и 110.
9.  Умножить двоичные числа 1011 и 1101.
10.  Поделить двоичное число 101010 на число 101.
11.  Поделить двоичное число 110110 на число 100.

## 1.

Напишите скрипт, который будет делать резервную копию файла. Резервный файл должен содержать дату создания в имени.

**Ответ**

```bash
@echo off
set "file_to_backup=myfile.txt"
set "backup_file=backup_%date:~6,4%%date:~3,2%%date:~0,2%%time:~0,2%%time:~3,2%%time:~6,2%.txt"
copy "%file_to_backup%" "%backup_file%"
echo Backup created: %backup_file%

```

## 2.

Напишите скрипт, который удалит файлы старше 30 дней в выбранной директории. Используйте утилиту  `forfiles`  для поиска и удаления файлов.

**Ответ**

```bash
@echo off
set "directory=C:\path\to\directory"
forfiles /P "%directory%" /S /D -30 /C "cmd /c if @isdir==FALSE del @file"
echo Files older than 30 days have been deleted.

```

В данном скрипте используется команда  `forfiles`  для поиска и удаления файлов.  `/P`  указывает директорию для поиска файлов,  `/S`  указывает поиск включая поддиректории,  `/D -30`  указывает, что нужно искать файлы, измененные более 30 дней назад, а  `/C "cmd /c if @isdir==FALSE del @file"`  указывает команду для удаления найденных файлов. После выполнения скрипта выводится сообщение о том, что файлы старше 30 дней были удалены.
## 3.

Напишите скрипт, который будет мониторить использование памяти определенным процессом, например, вашей программой, и ежесекундно записывать в файл объем использованной памяти. Используйте утилиту  `Tasklist`  для получения информации о процессе и  `find`  для фильтрации вывода.

**Ответ**

```batch
@echo off

set "output_file=memory_usage_log.txt"

REM Header for the output file (if it doesn't exist)
if not exist "%output_file%" echo "Datetime Memory_Usage(KB)" > "%output_file%"

REM Function to get memory usage of the process by PID
:get_memory_usage
for /f "skip=3 tokens=5" %%a in ('tasklist /fi "PID eq %1" /nh') do (
    echo %%a
    goto :eof
)

REM Check if a process ID was provided as an argument
if "%~1"=="" (
    echo "Usage: %~nx0 <process_id>"
    exit /b 1
)

REM Main loop to monitor and log memory usage
:main_loop
for /f "tokens=2 delims=," %%a in ('wmic process get processid^, workingsetsize /format:csv ^| find "%~1"') do (
    set "datetime=%date:~6,4%-%date:~3,2%-%date:~0,2% %time:~0,2%:%time:~3,2%:%time:~6,2%"
    set "memory_usage=%%a"
    echo %datetime% %memory_usage% >> "%output_file%"

    REM Wait for 1 second before the next iteration
    timeout /t 1 >nul
    goto :main_loop
)

```

## 4.

Напишите скрипт, который будет проверять доступность cайта. Это может пригодиться во многих приложениях, когда происходит отправка данных или работоспособность одного приложения зависит от другого, расположенного на другом сервере. Используйте утилиту  `curl`, которая позволяет делать запросы.

**Ответ**

```batch
@echo off
set "website=https://example.com"
curl -o NUL --silent --head --fail "%website%"
if %errorlevel% equ 0 (
    echo Website is reachable.
) else (
    echo Website is down or unreachable.
)
```
В данном скрипте используется команда  `curl`  с параметрами  `--head`  и  `--fail`  для отправки HEAD-запроса и проверки статуса ответа. Если статус успешный (код завершения 0), то выводится сообщение о том, что сайт доступен. В противном случае выводится сообщение о том, что сайт недоступен или недоступен.

