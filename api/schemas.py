from pydantic import BaseModel


class FakePersonalSchema(BaseModel):
    name: str
    address: str
    city: str
