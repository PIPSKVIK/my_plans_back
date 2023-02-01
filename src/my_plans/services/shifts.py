from fastapi import (
    Depends,
    HTTPException,
    status
)
from ..database import get_session
from sqlalchemy.orm import Session
from ..models.shifts import CreateShifts
from .. import tables


class ShiftsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_shift(self, user_id: int, data: CreateShifts) -> tables.Shifts:
        shifts_options = tables.Shifts(**data.dict(), user_id=user_id)
        self.session.add(shifts_options)
        self.session.commit()
        return shifts_options

