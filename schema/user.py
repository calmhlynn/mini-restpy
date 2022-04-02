from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import DateTime


class UserSchema(BaseModel):
    username: str = Field(title="", description="")
    password: str = Field(title="", description="")
    email: str = Field(title="", description="")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                # "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "username": "도로시",
                "password": "1234",
                "email": "orsar@nfp.com"
            }
        }


class UserResponse(BaseModel):
    id: UUID = Field(title="id", description="")
    username: str = Field(title="id", description="")
    password: str = Field(title="id", description="")
    email: str = Field(title="id", description="")
    # create_on: DateTime = Field(title="id", description="")

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True,
        schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "username": "도로시",
                "password": "1234",
                "email": "orsar@nfp.com"
            }
        }
