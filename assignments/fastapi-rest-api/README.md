# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI framework. You will create a simple task management API with basic CRUD operations, request validation, and proper HTTP status codes.

## 📝 Tasks

### 🛠️	Create Task Management API

#### Description
Build a REST API that manages a list of tasks. Each task should have an id, title, description, and completion status. Implement endpoints to create, read, update, and delete tasks.

#### Requirements
Completed program should:

- Define a Task model using Pydantic with fields: id (int), title (str), description (str), and completed (bool)
- Implement a GET `/tasks` endpoint that returns all tasks
- Implement a GET `/tasks/{task_id}` endpoint that returns a specific task by ID
- Implement a POST `/tasks` endpoint to create a new task
- Implement a PUT `/tasks/{task_id}` endpoint to update an existing task
- Implement a DELETE `/tasks/{task_id}` endpoint to remove a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️	Add Input Validation and Error Handling

#### Description
Enhance your API with proper input validation and error handling. Ensure that the API responds with meaningful error messages when invalid data is provided or when resources are not found.

#### Requirements
Completed program should:

- Validate that task titles are not empty and have a maximum length of 100 characters
- Validate that descriptions have a maximum length of 500 characters
- Return a 404 status code with an appropriate error message when a task is not found
- Return a 422 status code when validation fails with details about what went wrong
- Use Pydantic's built-in validation features for automatic input validation
