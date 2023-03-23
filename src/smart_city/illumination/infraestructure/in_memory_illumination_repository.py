import copy
from typing import List

from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.light_id import LightId
from illumination.domain.exceptions.light_not_found_exception import LightNotFoundException
from illumination.domain.illumination_repository import IlluminationRepository
from illumination.domain.entity.light import Light


class InMemoryIlluminationRepository(IlluminationRepository):

    def __init__(self) -> None:
        self.lights: dict[str, Light] = {}

    def get(self, light_id: LightId) -> Light:
        try:
            return copy.deepcopy(self.lights[str(light_id)])
        except KeyError as error:
            raise LightNotFoundException(
                f"Illumination with id={str(light_id)} not found!") from error

    def get_by_alias(self, light_alias: LightAlias) -> List[Light]:
        lights = [light for light in self.lights.values() if light.get_alias() == light_alias]
        if len(lights) == 0:
            raise LightNotFoundException(f"Illumination with alias={str(light_alias)} not found!")
        return copy.deepcopy(lights)

    def save(self, light: Light) -> None:
        self.lights[str(light.light_id)] = copy.deepcopy(light)
