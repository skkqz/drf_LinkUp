# API LinkUp

Это api для получения информации о пользователях и организациях.

## Подготовка к запуску API

### Клонировать репозиторий 

* Клонируйте этот репозиторий с помощью команды: `https://github.com/skkqz/drf_LinkUp`

### Создайте виртуальное окружение

* Выполните команду `python -m venv myenv`
* Активируйте виртуальное окружение 
  * Для операционной системы Linux или macOS: `source myenv/bin/activate`
  * Для операционной системы Windows:: `myenv\Scripts\activate.bat`

### Установите все зависимости

* Python 3.7 +
* Django 4.2
* djangorestframework 3.14.0
* Pillow 9.5.0
* Вы можете установить все зависимости одной командой: `pip install -r requirements.txt`

### Первый запуск API

* В директории проекта выполнить следующие действие:
    * `python manage.py makemigrations`
    * `python manage.py migrate`
* Запуск сервера:
    * `python manage.py runserver`

## Работа с API

### Получить списка всех пользователей и связанные с ними организации.

#### Request
~~~
GET /api/users/

http://localhost:8000/api/author/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
  {
      "id": 1,
      "email": "qwe@qwe.com",
      "first_name": "Ваня",
      "last_name": "Ванечкин",
      "telephone_number": "+721345652",
      "avatar": "http://127.0.0.1:8000/media/avatars/YrnhfVB35PczlPoZhbOE.jpg",
      "organizations": []
  },
  {
      "id": 4,
      "email": "mo@mo.com",
      "first_name": "Дима",
      "last_name": "Фокин",
      "telephone_number": "+78521459658",
      "avatar": "http://127.0.0.1:8000/media/avatars/preview.png",
      "organizations": [
          {
              "id": 1,
              "name": "ГазПром",
              "description": "Добыча нефтепродуктов"
          },
          {
              "id": 5,
              "name": "Вкусно и точка",
              "description": "Сеть ресторанов быстрого питания"
          }
      ]
  }
}
~~~

### Регистрация пользователя

#### Request
~~~
GET /api/users/reg/

http://localhost:8000/api/users/reg/
~~~

#### Response
~~~
HTTP 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "",
    "password": "",
    "password2": "",
    "first_name": "",
    "last_name": "",
    "telephone_number": "",
    "avatar": null
}
~~~

### Аутентификация пользователя

#### Request
~~~
GET /api/users/login/

http://localhost:8000/api/users/login/
~~~

#### Response
~~~
HTTP 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "",
    "password": ""
}
~~~

### Logout пользователя

#### Request
~~~
GET /api/users/logout/

http://localhost:8000/api/users/logout/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
~~~

### Профиль пользователя

#### Request
~~~
GET /api/users/profile/

http://localhost:8000/api/users/profile/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "email": "qwe@qwe.com",
    "first_name": "Ваня",
    "last_name": "Ванечкин",
    "telephone_number": "+721345652",
    "avatar": "http://127.0.0.1:8000/media/avatars/YrnhfVB35PczlPoZhbOE.jpg",
    "organizations": []
}
~~~

### Вывод одного пользователя по его ID, со списком связанных с ним организаций 

#### Request
~~~
GET /api/users/4/

http://localhost:8000/api/users/4/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "email": "mo@mo.com",
    "first_name": "Дима",
    "last_name": "Фокин",
    "telephone_number": "+78521459658",
    "avatar": "http://127.0.0.1:8000/media/avatars/preview.png",
    "organizations": [
        {
            "id": 1,
            "name": "ГазПром",
            "description": "Добыча нефтепродуктов"
        },
        {
            "id": 5,
            "name": "Вкусно и точка",
            "description": "Сеть ресторанов быстрого питания"
        }
    ]
}
~~~

### Вывод списка всех организаций и пользователей связанных с ней

#### Request
~~~
GET /api/organizations/

http://localhost:8000/api/organizations/
~~~

#### Response
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
  "id": 1,
  "name": "ГазПром",
  "description": "Добыча нефтепродуктов",
  "users": [
      {
          "id": 8,
          "email": "fafa@fafa.com",
          "first_name": Федя,
          "last_name": Гришкин,
          "telephone_number": +78521456532,
          "avatar": null
      },
      {
          "id": 4,
          "email": "mo@mo.com",
          "first_name": "Дима",
          "last_name": "Фокин",
          "telephone_number": "+78521459658",
          "avatar": "http://localhost:8000/media/avatars/preview.png"
      }
  ]
}

~~~

### Добавление новой организации 

#### Request
~~~
GET /api/organizations/create

http://localhost:8000/api/organizations/create
~~~

#### Response
~~~
HTTP 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "",
    "description": ""
}
~~~

### Участники проекта
* [skkqz](https://github.com/skkqz/)

Вы можете внести свой вклад в этот проект, создавая issues или pull requests.