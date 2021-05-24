# REST API для сервиса сокращения ссылок.

В данном проекте реализовано *REST API* для сервиса сокращения ссылок.

Проект написан на *Django/Django-Rest-Framework* и является тестовым заданием для компании **Делис Инфо**.

## Задание

**Задача**: Требуется написать REST API используя любой удобный фреймворк (предпочтительно flask/DRF/aiohttp).

**Обязательная часть**:

- API должен сокращать ссылки и предоставлять к ним доступ 
- Возможность удаления и т.д.
- Ссылки должны храниться в БД. БД может быть абсолютно любой, SQL/NoSQL.


**Необязательная часть**:

- Написать необходимые скрипты, чтоб все разворачивалось через docker-compose.

## Перед началом работы

1. Установите [Docker](https://www.docker.com/) на вашу операционную систему.
2. Установите [Docker Compose](https://docs.docker.com/compose)
    - Если на предыдущем шаге вы установили Docker Desktop, то этот шаг можно пропустить, т.к.
      Docker Compose установится автоматически

## Установка

1. Клонируйте репозиторий

```bash
$ git clone git@github.com:katorov/short-url-rest-api.git
$ cd short-url-rest-api
```

2. Переименуйте файл `.env-example` в `.env` и измените следующие значения на свои:

```bash
export DEBUG=True # Режим отладки
export SECRET_KEY='django-insecure-(8723e2j3h8752kd' # Секретный ключ
export BASE_SHORT_HOST='http://localhost:8000' # Хост для коротких ссылок
```

3. Поднимите докер-контейнеры

```bash
$ docker-compose up -d
```

Если не хватает прав для выполнения команды, попробуйте `$ sudo docker-compose up -d`

Для создания суперпользователя введите команду `docker exec -it shortener_app_web python manage.py createsuperuser` (*container_id* - идентификатор )

## Быстрый старт по API

### Получить сокращенные ссылки списком

Пример запроса
```bash
curl http://localhost:8000/api/short_link/ \
  -H 'Content-Type: application/json'
```

Пример ответа
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://ya.ru",
            "short_url": "http://localhost:8000/5"
        },
        {
            "url": "http://google.com",
            "short_url": "http://localhost:8000/6"
        }
    ]
}
```

### Добавить сокращенную ссылку

Пример запроса
```bash
curl http://localhost:8000/api/short_link/ \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{"url": "http://vk.com"}'
```

Пример ответа
```json
{
    "url": "http://vk.com",
    "short_url": "http://localhost:8000/49",
    "secret_key": "-1459097520421248900"
}
```

### Удалить сокращенную ссылку

Пример запроса
```bash
curl http://localhost:8000/api/short_link/49/?secret_key=-1459097520421248900 \
  -X DELETE
```