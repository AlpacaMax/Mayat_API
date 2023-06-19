from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Enum,
    DateTime,
    BOOLEAN,
)
from sqlalchemy.sql import func
import enum

from database import Base

class TaskStatus(enum.Enum):
    Running     = 1 # The task is created with the Running status
    Finished    = 2 # Once it's finished it enters Finished status
    Error       = 3 # Whatever possible errors occured when running

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.Running)
    datetime_created = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    result = Column(Text, default="")
    message = Column(Text, default="")