### Тестовое задание
Для запуска тестовых заданий
1. Установить виртуальное окружение
```
python -m venv venv
```
2. Активировать виртуальное окружение
```
venv\Scripts\activate.bat (Windows)

source venv/bin/activate (Linux/MacOS)
```
3. Установить зависимости requirements.txt
```
pip install -r requirements.txt
```

 Или
 
Если каталог проекта с тестовыми заданиями открывать через IDE (напр. PyCharm) - создайте окружение и установите все пакеты из requirements.txt.

##### №1 Парсинг JSON
Необходимые для парсинга данные есть в директории проекта.
Запустить файл "task1_parser.py".
Результатом испольнения будет файл "book.xlsx" в каталоге проекта.

##### #2 HTTP-запросы
Запустить файл "task2_request.py"
Следовать инструкциям в консоли - ввести значения "код ИФНС" и "ОКТМО"
Результат  будет выведен выведенная в консоли.

##### №3 SQL
Запустить файл "task3_db.py"
Результаты работы запросов будут выведены в консоли.
В каталоге проекта будет создан файл с БД "test_database.db".