from typing import Type

from sqlalchemy.orm import Session

from src.models import Task
import src.schemas as schemas


def get_all_task(db: Session) -> list[Type[Task]]:
    return db.query(Task).all()


def get_task_by_id(db: Session, task_id: int) -> Type[Task] | None:
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task: schemas.TaskBase) -> Task:
    task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    db.add(task)
    db.commit()
    return task


def update_task(db: Session, new_task: Task, task_id: int) -> Type[Task] | None:
    task = db.query(Task).filter(Task.id == task_id).first()

    task.title = new_task.title
    task.description = new_task.description
    task.completed = new_task.completed

    db.add(task)
    db.commit()
    return task


def delete_task_by_id(db: Session, task_id: int) -> Type[Task] | None:
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return task
