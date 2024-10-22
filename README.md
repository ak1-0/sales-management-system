![Work In Progress](https://img.shields.io/badge/Work%20In%20Progress-orange?style=flat-square)
## Внимание
⚠️ **Проект находится в стадии разработки.** ⚠️

# Sales Management System

## Описание
Система управления продажами для демонстрации навыков работы с Python и SQL.

## Установка
1. Клонировать репозиторий
2. Установить зависимости
3. Сгенерировать секретный ключ
```
import secrets
secret_key = secrets.token_hex(16)
print(secret_key)
```
4. Создайте .env
```
SECRET_KEY=
SQLALCHEMY_DATABASE_URI=
```
5. Выполнить команды для миграции базы данных
```
from app import db, create_app
app = create_app()
with app.app_context():
    db.create_all()
```
6.Запустить приложение

7. Пример заполнения формы на сайте:

Добавление продукта:
Product Name: "Laptop"
Price: "1000"

Добавление клиента:
First Name: "John"
Last Name: "Doe"
Email: "john.doe@example.com"
Phone: "123-456-7890"

Проведение продажи:
Product ID: "1"
Customer ID: "1"
Quantity: "2"

## Использование
Приложение позволяет добавлять продукты, клиентов и проводить продажи.