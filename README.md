# Проект Django с аутентификацией и CRUD для постов и комментариев

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/gremvanek/post_app.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd electronic_shop/post_app
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

## Работа с API через Postman

### 1. Регистрация пользователя

- **URL**: `http://localhost:8000/users/`
- **Метод**: POST
- **Тело запроса**:

    ```json
    {
        "login": "username",
        "email": "user@mail.ru",
        "password": "password123",
        "birth_date": "2000-01-01"
    }
    ```

### 2. Получение токена аутентификации

- **URL**: `http://localhost:8000/auth/token/login/`
- **Метод**: POST
- **Тело запроса**:

    ```json
    {
        "username": "username",
        "password": "password123"
    }
    ```

- **Ответ**:

    ```json
    {
        "token": "your-auth-token"
    }
    ```

### 3. Аутентификация с использованием токена

Для всех последующих запросов, которые требуют аутентификации, добавляйте заголовок `Authorization` с типом токена `Token`:

- **Заголовок**:

    ```
    Authorization: Token your-auth-token
    ```

### 4. Создание суперпользователя

- **URL**: `http://localhost:8000/users/create_superuser/`
- **Метод**: POST
- **Тело запроса**:

    ```json
    {
        "username": "admin",
        "email": "admin@mail.ru",
        "password": "adminpassword"
    }
    ```

### 5. Создание поста

- **URL**: `http://localhost:8000/post/posts/`
- **Метод**: POST
- **Тело запроса**:

    ```json
    {
        "title": "My First Post",
        "text": "This is the content of my first post.",
        "image": null
    }
    ```

- **Заголовок**:

    ```
    Authorization: Token your-auth-token
    ```

### 6. Создание комментария

- **URL**: `http://localhost:8000/post/comments/`
- **Метод**: POST
- **Тело запроса**:

    ```json
    {
        "text": "This is a comment on the post.",
        "post": 1
    }
    ```

- **Заголовок**:

    ```
    Authorization: Token your-auth-token
    ```

### 7. Выход из системы

Чтобы выйти из системы и удалить токен, отправьте POST-запрос на:

- **URL**: `http://localhost:8000/auth/token/logout/`
- **Метод**: POST
- **Заголовок**:

    ```
    Authorization: Token your-auth-token
    ```

## Примечание

Только авторизованные пользователи могут создавать, редактировать и удалять свои посты и комментарии. Администраторы имеют право редактировать и удалять любые посты и комментарии.

Этот README включает все необходимые шаги для регистрации пользователя, получения токена аутентификации, создания суперпользователя, а также выполнения CRUD-операций с постами и комментариями через Postman.
