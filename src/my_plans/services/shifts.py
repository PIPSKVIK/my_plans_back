from typing import List
from fastapi import (
    Depends,
    HTTPException,
    status
)
from ..database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import extract
from ..models.shifts import CreateShifts, BaseShifts, TypeShifts
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

    def update_shifts(self, shift_id: int, request_shift_data: BaseShifts) -> tables.Shifts:
        shift_options = (
            self.session
            .query(tables.Shifts)
            .filter_by(id=shift_id)
            .first()
        )
        for field, value in request_shift_data:
            setattr(shift_options, field, value)
        self.session.commit()
        return shift_options

    def delete_shift(self, shift_id: int):
        request_shift = (
            self.session
            .query(tables.Shifts)
            .filter_by(id=shift_id)
            .first()
        )
        self.session.delete(request_shift)
        self.session.commit()

    def get_current_shift_by_id(self, shift_id: int) -> tables.Shifts:
        shift = (
            self.session
            .query(tables.Shifts)
            .filter_by(id=shift_id)
            .first()
        )
        return shift
