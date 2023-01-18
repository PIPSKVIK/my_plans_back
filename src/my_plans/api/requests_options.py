from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from ..models.requests_options import (
    RequestOptions,
    RequestOptionsUpdate,
    RequestOptionsCreate
)
from ..services.auth import get_current_user

from ..services.requests_options import RequestOptionsService
from ..tables import User

router = APIRouter(
    prefix='/request-options'
)


@router.get('/', response_model=List[RequestOptions], tags=["options_api"])
def get_request_options(
    user: User = Depends(get_current_user),
    service: RequestOptionsService = Depends()
):
    return service.get_list(user_id=user.id)


@router.get('/{request_option_id}', response_model=RequestOptions, tags=["options_api"])
def get_request_option(
    request_option_id: int,
    user: User = Depends(get_current_user),
    service: RequestOptionsService = Depends()
):
    return service.get(user_id=user.id, request_option_id=request_option_id)


@router.post('/', response_model=RequestOptions, tags=["options_api"])
def create_request(
    data: RequestOptionsCreate,
    user: User = Depends(get_current_user),
    service: RequestOptionsService = Depends()
):
    return service.create(user_id=user.id, data=data)


@router.put('/{request_option_id}', response_model=RequestOptions, tags=["options_api"])
def update_request_option(
    request_option_id: int,
    request_option_data: RequestOptionsUpdate,
    user: User = Depends(get_current_user),
    service: RequestOptionsService = Depends()
):
    return service.update(
        user_id=user.id,
        request_option_id=request_option_id,
        request_option_data=request_option_data
    )


@router.delete('/{request_option_id}', tags=["options_api"])
def delete_request_option(
    request_option_id: int,
    user: User = Depends(get_current_user),
    service: RequestOptionsService = Depends()
):
    service.delete(user_id=user.id, request_option_id=request_option_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

