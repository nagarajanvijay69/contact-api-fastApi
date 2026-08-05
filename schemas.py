from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str
    email: str
    phone: str


class ContactUpdate(BaseModel):
    name: str | None=None
    email: str | None=None
    phone: str| None=None

class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str   

    model_config = {
        "from_attributes": True
    }