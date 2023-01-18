from pydantic import BaseModel
from datetime import date
from datetime import time
from enum import Enum


class RequestStatus(str, Enum):
    DECLINE = 'decline'
    ACCEPTED = 'accept'
    UNDER_CONSIDERATION = 'under consideration'


class Request(BaseModel):
    id: int
    date: date
    time: time
    hours: int
    reason: str
    status: RequestStatus
    note: str

