"""
FastAPI Task Management API - Starter Code

Complete this API by implementing the missing endpoints and validation.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Task Management API")

# TODO: Define the Task model using Pydantic
# The Task should have: id (int), title (str), description (str), completed (bool)
class Task(BaseModel):
    pass


# In-memory storage for tasks (for demonstration purposes)
tasks_db = []
task_id_counter = 1


@app.get("/")
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}


# TODO: Implement GET /tasks endpoint to return all tasks
@app.get("/tasks")
def get_all_tasks():
    pass


# TODO: Implement GET /tasks/{task_id} endpoint to return a specific task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


# TODO: Implement POST /tasks endpoint to create a new task
@app.post("/tasks", status_code=201)
def create_task():
    pass


# TODO: Implement PUT /tasks/{task_id} endpoint to update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    pass


# TODO: Implement DELETE /tasks/{task_id} endpoint to delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass
