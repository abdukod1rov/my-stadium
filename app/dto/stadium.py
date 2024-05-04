from datetime import datetime
from typing import Union

from pydantic import BaseModel


def serialize_time(value: datetime) -> str:
    return value.strftime('%d.%m.%Y %H:%M')


class StadiumBase(BaseModel):
    name: str
    city: str
    price: float

    class Config:
        json_encoders = {
            datetime: serialize_time
        }
        from_attributes = True
        orm_mode = True
        populate_by_name = True


class StadiumCreate(StadiumBase):
    capacity: int
    country: str
    description: Union[None, str] = None
    time_start: str
    time_end: str
    status: Union[str, None] = None
    type: Union[str, None] = None


class StadiumOut(StadiumCreate):
    id: int
    owner_id: int


class UpdateStadium(BaseModel):
    capacity: Union[int, None] = None
    country: Union[None, str] = None
    description: Union[None, str] = None
    time_start: Union[str, None] = None
    time_end: Union[str, None] = None
    name: Union[str, None] = None
    status: Union[str, None] = None

