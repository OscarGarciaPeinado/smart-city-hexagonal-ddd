from typing import List

from kink import inject

from illumination.domain.entity.light import Light
from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.illumination_repository import IlluminationRepository


@inject
class TurnLight:
    def __init__(self, illumination_repository: IlluminationRepository):
        self.illumination_repository = illumination_repository

    def turn_light(self, light_alias: LightAlias) -> None:
        lights: list[Light] = self.illumination_repository.get_by_alias(light_alias)
        for light in lights:
            light.turn()
            self.illumination_repository.save(light)
