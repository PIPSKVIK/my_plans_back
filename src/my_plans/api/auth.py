from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.auth import (
    User,
    UserCreate,
    Token,
    BaseUser
)
from ..services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth'
)


# Регистрация
@router.post('/sign-up', response_model=Token, tags=["users_api"])
def sign_up(
    user_data: UserCreate,
    service: AuthService = Depends()
):
    return service.register_new_user(user_data)


# Авторизация
@router.post('/sign-in', response_model=Token, tags=["users_api"])
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )


# Получение пользователя
@router.get('/user', response_model=User, tags=["users_api"])
def get_user(user: User = Depends(get_current_user)):
    return user


@router.get('/users', response_model=List[User], tags=["users_api"])
def get_all_users(
    user: User = Depends(get_current_user),
    service: AuthService = Depends()
):
    return service.get_all_users()


@router.get('/user/{user_id}', response_model=User, tags=["users_api"])
def get_user_by_id(
    user_id: int,
    user: User = Depends(get_current_user),
    service: AuthService = Depends()
):
    return service.get_user_by_id(user_id)

# @router.get(
#     '/{operation_id}',
#     response_model=models.Operation,
# )
# def get_operation(
#     operation_id: int,
#     user: models.User = Depends(get_current_user),
#     operations_service: OperationsService = Depends(),
# ):
#     return operations_service.get(
#         user.id,
#         operation_id,
#     )
