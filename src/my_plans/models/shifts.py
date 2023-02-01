from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class TypeShifts(str, Enum):
    JOB = 'job'
    FAMILY = 'family'
    PERSONAL_TIME = 'personal time'
    ENTERTAINMENT = 'entertainment'
    SPORT = 'sport'
    LEARNING = 'larning'
    TRAVEL = 'travel'


class StatusShifts(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'
    PAUSE = 'pause'


class BaseShifts(BaseModel):
    name: str
    start_at: date
    end_at: date
    comment: Optional[str]
    type: TypeShifts
    is_anomaly_time: Optional[bool] = False
    location: str
    isEnded: Optional[bool] = False
    status: StatusShifts


class Shifts(BaseShifts):
    id: int

    class Config:
        orm_mode = True


class CreateShifts(BaseShifts):
    pass
