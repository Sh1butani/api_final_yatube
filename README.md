### Описание:
API для социальной сети YaTube.

- Возможность просмотра, создания, редактирования и удаления публикаций.
- Просмотр и создание групп.
- Возможность добавления, редактирования и удаления комментариев.
- Подписки на пользователей.
- Для аутентификации используются JWT-токены.

### Технологии:

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.9.10%20-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v3.2.16-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Sh1butani/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API:

Получение списка всех публикаций:
GET /api/v1/posts/

Добавление нового комментария к публикации:
POST /api/v1/posts/{post_id}/comments/

Получение списка доступных сообществ:
GET /api/v1/groups/

Получение всех подписок пользователя, сделавшего запрос:
GET /api/v1/follow/


Полный перечень запросов вы можете найти в документации к API, доступной после запуска сервера
по адресу: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) 

### Автор:
[David Pilosyan](https://t.me/Shibutani)