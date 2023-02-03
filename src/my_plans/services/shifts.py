from typing import List
from fastapi import (
    Depends,
    HTTPException,
    status
)
from ..database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import extract
from ..models.shifts import CreateShifts
from .. import tables

from datetime import date
from datetime import datetime


class ShiftsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_shift(self, user_id: int, data: CreateShifts) -> tables.Shifts:
        shifts_options = tables.Shifts(**data.dict(), user_id=user_id)
        self.session.add(shifts_options)
        self.session.commit()
        return shifts_options

    def get_all_shifts(self) -> List[tables.Shifts]:
        shifts_options = (
            self.session
            .query(tables.Shifts)
            .all()
        )
        return shifts_options

    def get_shifts_by_month(self, month: int) -> List[tables.Shifts]:
        shifts = (
            self.session
            .query(tables.Shifts)
            .filter_by(month=month)
            .all()
        )
        return shifts
