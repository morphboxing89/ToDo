from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str]
    completed: Optional[bool]


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
