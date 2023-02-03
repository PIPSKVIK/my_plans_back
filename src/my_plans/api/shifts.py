from typing import List

from fastapi import APIRouter
from fastapi import Depends
from ..models.shifts import (Shifts, CreateShifts, BaseShifts)
from ..services.auth import get_current_user

from ..tables import User
from ..services.shifts import ShiftsService

router = APIRouter(
    prefix='/shifts'
)


@router.post('/', response_model=Shifts, tags=["shifts_api"])
def create_shifts(
    data: CreateShifts,
    user: User = Depends(get_current_user),
    service: ShiftsService = Depends()
):
    return service.create_shift(user_id=user.id, data=data)


@router.get('/', response_model=List[Shifts], tags=["shifts_api"])
def get_all_shifts(
    user: User = Depends(get_current_user),
    service: ShiftsService = Depends()
):
    return service.get_all_shifts()


@router.get('/shifts-by-month{month}', response_model=List[Shifts], tags=["shifts_api"])
def get_shifts_by_month(
        month: int,
        user: User = Depends(get_current_user),
        service: ShiftsService = Depends()
):
    return service.get_shifts_by_month(month=month)
