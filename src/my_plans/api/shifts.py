from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from ..models.shifts import (Shifts, CreateShifts, BaseShifts, TypeShifts)
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


@router.get('/shifts-by-month/{month}', response_model=List[Shifts], tags=["shifts_api"])
def get_shifts_by_month(
        month: int,
        user: User = Depends(get_current_user),
        service: ShiftsService = Depends()
):
    return service.get_shifts_by_month(month=month)


@router.put('/{shift_id}', response_model=Shifts, tags=["shifts_api"])
def update_shifts(
    shift_id: int,
    request_shift_data: BaseShifts,
    user: User = Depends(get_current_user),
    service: ShiftsService = Depends()
):
    return service.update_shifts(
        shift_id=shift_id,
        request_shift_data=request_shift_data
    )


@router.delete('/{shift_id}', tags=["shifts_api"])
def delete_shift(
    shift_id: int,
    user: User = Depends(get_current_user),
    service: ShiftsService = Depends()
):
    service.delete_shift(shift_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
