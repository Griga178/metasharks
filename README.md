# Запуск: 

### Установить библиотеки:
pip install -r requirements.txt

### Подключить БД:

settings.py - DATABASES  

### Запустить миграции:
- manage.py makemigrations
- manage.py migrate

### Заполнить тестовыми данными
- post_info.py (примеры post запросов)
- get_info.py (примеры get запросов)

### Тут таблица заказов с сортировкой и фильтром
`http://127.0.0.1:8000/api/`

### Тут описание API Swagger
http://127.0.0.1:8000/swagger/
