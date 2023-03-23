from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from kink import di
from illumination.application.create.create_light_command_dto import CreateLightCommandDto
from illumination.application.create.light_creator import LightCreator
from illumination.application.turn.turn_light import TurnLight
from illumination.application.turn.turn_light_command_dto import TurnLightCommandDto
from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.location import Location
from illumination.domain.exceptions.light_not_found_exception import LightNotFoundException
from illumination.domain.exceptions.malformed_location_exception import MalformedLocationException
from shared.domain.api_error_message import APIErrorMessage

router = APIRouter()


@router.post(
    "/light",
    responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}},
    tags=["light"],
)
async def create_light(request: CreateLightCommandDto,
                       creator: LightCreator = Depends(lambda: di[LightCreator])) -> JSONResponse:
    try:
        light = creator.create(LightAlias(request.alias),
                               Location(request.latitude, request.longitude))

    except MalformedLocationException as e:
        return JSONResponse(content={"error": "Malformed location"},
                            status_code=status.HTTP_406_NOT_ACCEPTABLE)

    return JSONResponse(content={"light_id": str(light.light_id)}, status_code=status.HTTP_200_OK)


@router.put(
    "/turn_light",
    responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}},
    tags=["turn_light"],
)
async def turn_light(request: TurnLightCommandDto,
                     turn_light: TurnLight = Depends(lambda: di[TurnLight])) -> JSONResponse:
    try:
        turn_light.turn_light(LightAlias(request.alias))
    except LightNotFoundException as e:
        return JSONResponse(content={"error": "Light not found"},
                            status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content={"message": "Turn lights successfully"},
                        status_code=status.HTTP_200_OK)
