# Запуск:

## Установить библиотеки:
pip install -r requirements.txt

## Подключить БД:
### metasharks
### ├── sharkstest
### │   ├── sharkstest
### │   ├── sharkstest
### │   ├── settings.py - DATABASES  <-- ТУТ

## Запустить миграции:
- manage.py makemigrations
- manage.py migrate

## Заполнить тестовыми данными
- post_info.py

### Тут таблица заказов с сортировкой и фильтром
`http://127.0.0.1:8000/api/`
