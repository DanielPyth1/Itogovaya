Тестовое задание для старта трудоустройства № 1

API для управления сетью по продаже электроники, созданный с использованием Django и Django Rest Framework. 
Проект поддерживает трёхуровневую иерархию и CRUD-операции для узлов сети и продуктов.

Особенности:
- Реализованы методы CRUD для моделей "Узлы сети" и "Продукты".
- Фильтрация узлов сети по стране
- Админка для управления объектами с фильтрацией и действиями.
- Поддержка базы данных PostgreSQL.

Технические требования:
Python 3.8+
Django 3+
DRF 3.10+
PostgreSQL 10+

Откройте браузер и перейдите по адресу:
http://127.0.0.1:8000/admin/ — Админка.
http://127.0.0.1:8000/api/ — API.

Модели

Узлы сети (Network Nodes):
name — Название (обязательно).
email — Email.
country — Страна.
city — Город.
street — Улица.
house_number — Номер дома.
level — Уровень иерархии (0: Завод, 1: Розничная сеть, 2: Индивидуальный предприниматель).
supplier — Поставщик (ForeignKey на другой узел сети).
debt — Задолженность перед поставщиком.
created_at — Дата создания (автоматически).

Продукты (Products):
name — Название продукта.
model — Модель.
release_date — Дата выхода на рынок.
network_node — Связанный узел сети (ForeignKey).


Эндпоинты

Узлы сети (Network Nodes):
GET /api/nodes/ — Получить список всех узлов сети.
POST /api/nodes/ — Создать новый узел сети.
GET /api/nodes/{id}/ — Получить данные конкретного узла.
PUT /api/nodes/{id}/ — Обновить узел.
PATCH /api/nodes/{id}/ — Частично обновить узел.
DELETE /api/nodes/{id}/ — Удалить узел.

Продукты (Products):
GET /api/products/ — Получить список всех продуктов.
POST /api/products/ — Создать новый продукт.
GET /api/products/{id}/ — Получить данные конкретного продукта.
PUT /api/products/{id}/ — Обновить продукт.
PATCH /api/products/{id}/ — Частично обновить продукт.
DELETE /api/products/{id}/ — Удалить продукт.

Функционал админки:
- Управление узлами сети и продуктами.
- Фильтрация узлов сети по городу
- Фильтрация продуктов по дате выхода продукта на рынок
- Действие "Очистить задолженность перед поставщиком" для узлов сети.
- Ссылка на "Поставщика"

Автор: Жиров Даниил
Email: danieelpark@gmail.com
GitHub: https://github.com/DanielPyth1/
