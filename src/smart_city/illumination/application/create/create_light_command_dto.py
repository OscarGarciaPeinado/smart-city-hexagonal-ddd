from pydantic import BaseModel


class CreateLightCommandDto(BaseModel):
    alias: str
    latitude: int
    longitude: int
