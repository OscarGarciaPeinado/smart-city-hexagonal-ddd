from pydantic import BaseModel


class TurnLightCommandDto(BaseModel):
    alias: str
