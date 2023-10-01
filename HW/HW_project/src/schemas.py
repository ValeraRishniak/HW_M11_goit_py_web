from datetime import datetime, date
from pydantic import BaseModel

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str = None


class ContactResponse(ContactBase):
    id: int = 1
    first_name: str = "Dow"
    last_name: str = "John"
    email: str = "example@test.com"
    phone_number: str = "5551234567"
    birthday: date = date(year=1999, month=10, day=5)
    additional_data: str = "Created first contact for test"

    class Config:
        orm_mode = True