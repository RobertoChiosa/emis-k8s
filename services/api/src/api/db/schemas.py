from pydantic import BaseModel


class User(BaseModel):
    email: str
    id: int
    is_active: bool
