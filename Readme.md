# FastAPI Todo Application

![Python 3](https://img.shields.io/badge/Python-3-green.svg?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)

This is a basic API for a todo application made with FastAPI. You can use any frontend framework with this. I am using SQLite in this project. Other databases can also be used easily. <a href="https://fastapi.tiangolo.com/tutorial/sql-databases/">Refer to this</a> for more information on how to use other databases with FastAPI.

## API endpoints:

- Get all the todo items present in the database, send a get request on the following endpoint:

```
http://127.0.0.1:8000/todos
```

- To post a todo item in the database, send a post request on the following endpoint:

```
http://127.0.0.1:8000/todos
```

- To update a specific todo item as completed/pending, send a put request on the following endpoint:

```
http://127.0.0.1:8000/todos/<todoItemID>
```

For further details, you can refer to <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a> after starting the server. It will give you an auto generated and very detailed documentation.
