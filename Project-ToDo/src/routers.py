from typing import Annotated

from fastapi import APIRouter, Depends
from src.database import SessionLocal

import src.utils as utils
from src.schemas import TaskBase, Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get('/', response_model=list[TaskBase])
async def get_tasks():
    with SessionLocal() as session:
        tasks = utils.get_all_task(session)
    return tasks


# @router.get('/', response_model=Task)
# async def get_tasks_id(task_id: int):
#     with SessionLocal() as session:
#         session.expire_on_commit = False
#         tasks = utils.get_task_by_id(session, task_id)
#     return tasks


@router.post('/', response_model=Task)
async def create_tasks(task: Annotated[TaskBase, Depends()]):
    with SessionLocal() as session:
        session.expire_on_commit = False
        task = utils.create_task(session, task)
    return task


@router.put('/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Annotated[TaskBase, Depends()]):
    with SessionLocal() as session:
        session.expire_on_commit = False
        task = utils.update_task(session, task, task_id)
    return task


@router.delete('/{task_id}', response_model=Task)
async def delete_task(task_id: int):
    with SessionLocal() as session:
        session.expire_on_commit = False
        task = utils.delete_task_by_id(session, task_id)
    return task