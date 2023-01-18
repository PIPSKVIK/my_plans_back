from typing import List

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from ..models.requests_options import (
    RequestOptionsCreate,
    RequestOptionsUpdate
)
from ..database import get_session

from .. import tables


class RequestOptionsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int) -> List[tables.RequestOptions]:
        request_options = (
            self.session
            .query(tables.RequestOptions, user_id=user_id)
            .all()
        )
        return request_options

    def get(self, user_id: int, request_option_id: int) -> tables.RequestOptions:
        request_option = (
            self.session
            .query(tables.RequestOptions)
            .filter_by(id=request_option_id, user_id=user_id)
            .first()
        )
        if not request_option:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return request_option

    def create(self, user_id: int, data: RequestOptionsCreate) -> tables.RequestOptions:
        request_options = tables.RequestOptions(**data.dict(), user_id=user_id)
        self.session.add(request_options)
        self.session.commit()
        return request_options

    def update(
        self,
        user_id: int,
        request_option_id: int,
        request_option_data: RequestOptionsUpdate
    ) -> tables.RequestOptions:
        request_option = (
            self.session
            .query(tables.RequestOptions)
            .filter_by(id=request_option_id, user_id=user_id)
            .first()
        )

        for field, value in request_option_data:
            setattr(request_option, field, value)
        self.session.commit()
        return request_option

    def delete(self, user_id: int, request_option_id: int):
        request_option = (
            self.session
            .query(tables.RequestOptions)
            .filter_by(id=request_option_id, user_id=user_id)
            .first()
        )
        self.session.delete(request_option)
        self.session.commit()
