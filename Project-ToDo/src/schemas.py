from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
