from pydantic import BaseModel


class RequestOptions(BaseModel):
    id: int
    request_name: str

    class Config:
        orm_mode = True


class RequestOptionsCreate(BaseModel):
    request_name: str


class RequestOptionsUpdate(BaseModel):
    request_name: str
