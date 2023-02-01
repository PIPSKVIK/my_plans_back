from fastapi import APIRouter
from fastapi import Depends
from ..models.shifts import (Shifts, CreateShifts)
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
