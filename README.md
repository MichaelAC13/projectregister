# FLASK BASIC STRUCT FOR HEROKU

In the project directory, you can run:

```bash
    python -m venv env
```

For activate script:

```bash
    ./env/Scripts/activate`
```
Runs the app in the development mode.\

```bash
    python app.py
```
Have fun!

FLASK API V1.0.0
API to serve application for professionals who have the need to point hours of work in associated projects.

The examples below assume that the token is correctly coming through the request header, and that it is using the route with the updated api version.

POST
AutValid User
http://127.0.0.1:5001/api/v1.0.0/authenticate
When authenticating a user, a token is generated that must be kept somewhere private to serve as an access key for the other private routes. The Token is not configured to expire but it is possible to implement this.

Request Headers
Bodyraw (json)
json
{
  "login": "login2",
  "password": "123456"
}
POST
Authentication - Invalid User
http://127.0.0.1:5001/api/v1.0.0/authenticate
When the user cannot be authenticated, an error is returned stating that the request was successful but the user has not yet been registered. In case any element of the jeson da object is missing or there is an error in the keys, an error is returned.

Bodyraw (json)
json
{
  "login": "NONEXISTENT",
  "password": "12345"
}
POST
Time Record - Valid keys
https://registerprogects.herokuapp.com/api/v1.0.0/times
New times are recorded normally if the json data is correct. Registration is only done if there is no project with the same user id and/or project id. If you try to register a time with a user or project already registered, the system will only update the time.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklOR0BnbWFpbC5jb20iLCJsb2dpbiI6Ik1pY2hhZWwiLCJuYW1lIjoiTWljaGFlbCIsInVzZXJfaWQiOiIxNiJ9.nZ2xY3olbITI_ltQ3bsg1vc-kpopTdox4BFdx2dzZa8
Bodyraw (json)
json
{
  "project_id": "1",
  "user_id": "3",
  "started_at": "2022-07-13 12:39:23.472727",
  "ended_at": "2022-07-13 16:32:23.472727"
}
POST
Time Record - Invalid keys
http://127.0.0.1:5001/api/v1.0.0/times
Key error example.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "project_idERROR": "1",
  "user_id": "1",
  "started_at": "2022-07-13 16:31:23.472727",
  "ended_at": "2022-07-13 16:31:23.472727"
}
POST
User - Create User
https://registerprogects.herokuapp.com/api/v1.0.0/users
To check the existence of a user is considered login and password only.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "name": "Michael",
  "email": "STRING@gmail.com",
  "login": "Michael",
  "password": "Mic123#"
}
POST
User - Create User - with existing user
http://127.0.0.1:5001/api/v1.0.0/users
When a user exists it cannot be registered again. There is another route to update the data.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "name": "USERsss",
  "email": "STRING@gmail.com",
  "login": "newuser",
  "password": "ST123456"
}
GET
User - Fetching data by existing id
http://127.0.0.1:5001/api/v1.0.0/users/1
Fetching data by existing id.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
GET
User - Fetching data by non-existing id
http://127.0.0.1:5001/api/v1.0.0/users/200
When searching for non-existent data, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
PUT
User - Changing and querying
http://127.0.0.1:5001/api/v1.0.0/users/2
User data is compensated and returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "name": "USER",
  "email": "STRING@gmail.com",
  "login": "USER",
  "password": "ST123456"
}
PUT
User - Changing and querying with non-existing id
http://127.0.0.1:5001/api/v1.0.0/users/200
When the id does not exist, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "name": "USER",
  "email": "STRING@gmail.com",
  "login": "USER",
  "password": "ST123456"
}
GET
Projects - Querying
http://127.0.0.1:5001/api/v1.0.0/projects
Consult the list of registered projects.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
GET
Projects - Fetching data by id
http://127.0.0.1:5001/api/v1.0.0/projects/1
Query project with indicated id.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
GET
Projects - Fetching data by non-existing id
http://127.0.0.1:5001/api/v1.0.0/projects
When the id does not exist, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
POST
Projects - Creating and querying
http://127.0.0.1:5001/api/v1.0.0/projects
Create project with JSON data following previous error handling pattern.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
POST
Projects - Creating and querying with existing project
http://127.0.0.1:5001/api/v1.0.0/projects
You can only create projects with new titles. If it is necessary to update data from a project it is possible using another route.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
PUT
Projects - Changing and querying
http://127.0.0.1:5001/api/v1.0.0/projects/1
Update your project data.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
PUT
Projects - Changing and querying with non-existing project
http://127.0.0.1:5001/api/v1.0.0/projects/111
When the id does not exist, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
GET
Times - Fetching data by id
http://127.0.0.1:5001/api/v1.0.0/times/1
Query time with indicated id.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
GET
Times - Fetching data by non-existing id
http://127.0.0.1:5001/api/v1.0.0/times/10000
When the id does not exist, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "title": "a1s2",
  "description": "a2",
  "user_id": "[1,2,3,5]"
}
PUT
Times - Changing and querying
http://127.0.0.1:5001/api/v1.0.0/times/1
Change the data of a time using the id.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "project_id": 1,
  "user_id": 2,
  "started_at": "2022-07-14 10:27:05.608750",
  "ended_at": "2022-07-15 10:27:05.608750"
}
PUT
Times - Changing and querying by non-existing id
http://127.0.0.1:5001/api/v1.0.0/times/112
When the id does not exist, an error is returned.

Request Headers
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IlNUUklORyIsImxvZ2luIjoibG9naW4yIiwibmFtZSI6IlNUUklORyIsInVzZXJfaWQiOiIzIn0.HhD35L9rh69v3Mot6cZM_QB2GMWdWiGsFb_jVmbPV0o
Bodyraw (json)
json
{
  "project_id": 1,
  "user_id": 2,
  "started_at": "2022-07-14 10:27:05.608750",
  "ended_at": "2022-07-15 10:27:05.608750"
}
