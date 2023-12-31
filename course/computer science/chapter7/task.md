# Курс: Информатика
#computer_science #python #practice 

# Практическое задание №7. " VCSs"

# 1. В начале

### 1.1. Настройте свое имя и электронную почту

```bash
git config --global user.name  "Your Name"
git config --global user.email your@email.com
```

### 1.2. Установка кэширования пароля

```bash
git config credential.helper 'cache --timeout=3600'
```

Если вы не установите этот параметр, то вам придется вводить имя пользователя и пароль каждый раз, когда при выполнении команды `git push`. Таймаут задается в секундах. По истечении этого времени `git` снова запросит ваше имя пользователя и пароль. Приведенная выше команда устанавливает тайм-аут на **10 часов**.
### 1.3. Клонирование git-репозитория с github

```bash
git clone https://github.com/kubenet/course_embedded_systems.git
```

# 2. Цикл разработки

### 2.1. Обновление своей копии файлов репозитория с учетом изменений, внесенных другими людьми

```bash
git pull
```

### 2.2. Добавление новых файлов или каталогов (рекурсивно)

```bash
git add file_or_directory_name
```

### 2.3. Редактирование файлов

### 2.4. Проверка состояния перед регистрацией

Отмечайте измененные, добавленные, удаленные файлы.
Отметьте файлы, которые вы собирались добавить, но забыли это сделать.

```bash
git status
```

### 2.5. Сверьте дифферент с репозиторием, чтобы просмотреть свои изменения в коде

```bash
git diff
```

### 2.6. Убедитесь, что в тексте нет табуляции

Разные редакторы по-разному относятся к вкладкам, и многим пользователям это не нравится.
Разработчикам не следует настраивать ширину вкладок в своих текстовых редакторах для того, чтобы иметь возможность читать исходный текст.
Существуют некоторые исключения, в частности, Makefiles.
Чтобы найти табуляции в текстовых файлах, можно воспользоваться следующей командой:

```bash
grep -rlI --exclude-dir=.git --exclude=*.mk $'\t' .
```

Значение опций grep:

* -r - рекурсивный
* -l - список файлов
* -I - игнорировать двоичные файлы

Вы можете исправить вкладки, выполнив следующие действия, но обязательно просмотрите исправления:

```bash
grep -rlI --exclude-dir=.git --exclude=*.mk $'\t' . | xargs sed -i 's/\t/    /g'
```

### 2.7. Если вы хотите отменить незафиксированные изменения в файле или каталоге, используйте эту команду:

```bash
git checkout file_or_directory_name
```

### 2.8. Если вы хотите отменить незафиксированные изменения для всех файлов в текущем каталоге, включая незафиксированные удаления, используйте эту команду:

```bash
git checkout .
```

### 2.9. Если вы хотите отменить какие-либо зафиксированные или даже перенесенные изменения, обратитесь к опытному пользователю git или внимательно прочитайте документацию по git, убедившись, что вам все понятно.

### 2.10. После завершения редактирования зафиксируйте

Обратите внимание, что опция -a автоматически ставит на очередь все модификации и удаления файлов, но не добавления.
Для явного добавления файлов или каталогов необходимо использовать 'git add'.

**Важное замечание 1: Перед любой фиксацией выполняйте команды "git status" и "git diff".
Отмена зафиксированных и, особенно, сдвинутых изменений сложнее, чем отмена нефиксированных изменений**.

**Важное замечание 2: Пожалуйста, ставьте осмысленный комментарий к каждой фиксации.**

```bash
git commit -a -m "A meaningful comment"
```

### 2.11. Официально опубликуйте все зафиксированные изменения в git-репозитории (например, GitHub).
Теперь все смогут увидеть ваши изменения.

```bash
git push
```

# 3. Другие виды практики

### 3.1. Просмотреть историю репозитория можно на самом сайте http://github.com с помощью интерфейса веб-браузера

### 3.2. Если вам нужно, чтобы Git игнорировал некоторые файлы, поместите их в .gitignore

Такие файлы могут включать автоматически сгенерированные двоичные файлы, временные файлы,
или несвязанные файлы, которые вы не хотите регистрировать или отображать в статусе git.
Пожалуйста, перед этим прочитайте о .gitignore в документации Git.

### 3.3. Если вы хотите увидеть файлы в вашем дереве, не отслеживаемые Git'ом, воспользуйтесь командой:

```bash
git clean -d -n
```

Эта команда работает от текущего каталога вниз.

После просмотра (будьте внимательны!) вы можете удалить файлы, выполнив команду:

```bash
git clean -d -f
```

### 3.4.  Если вы хотите увидеть файлы в вашем дереве, игнорируемые Git'ом

Для поддержания чистоты периодически удаляйте файлы в дереве,
игнорируемые git'ом на основании списка .gitignore.
Их обязательно нужно удалять перед подготовкой релиз-пакета.

```bash
git clean -d -x -n
```

После просмотра (будьте внимательны!) вы можете удалить файлы, выполнив команду:


```bash
git clean -d -x -f
```

### 3.5. Если вам необходимо выполнить какие-либо нетривиальные действия (слияние, отмена зафиксированных или перенесенных изменений), внимательно изучите документацию по Git.

В противном случае вы можете внести беспорядок, ошибки или проверить большие бинарные файлы, загрязняющие репозиторий.
