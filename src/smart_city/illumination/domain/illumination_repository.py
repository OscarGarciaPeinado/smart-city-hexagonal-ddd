from abc import ABC, abstractmethod
from typing import List

from illumination.domain.entity.light import Light
from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.light_id import LightId


class IlluminationRepository(ABC):
    @abstractmethod
    def get(self, light_id: LightId) -> Light:
        ...

    @abstractmethod
    def get_by_alias(self, light_alias: LightAlias) -> List[Light]:
        ...

    @abstractmethod
    def save(self, ligth: Light) -> None:
        ...
