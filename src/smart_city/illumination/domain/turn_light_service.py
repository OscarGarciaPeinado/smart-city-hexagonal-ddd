from abc import ABC, abstractmethod

from illumination.application.TurnLightDTO import TurnLightDTO


class LightService(ABC):

    @abstractmethod
    def turn_light(self, turn_light_dto: TurnLightDTO) -> None:
        ...
