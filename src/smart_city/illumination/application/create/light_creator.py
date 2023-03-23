from kink import inject

from illumination.domain.illumination_repository import IlluminationRepository
from illumination.domain.entity.light import Light
from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.light_status import LightStatus
from illumination.domain.entity.location import Location
from shared.domain.bus_publisher import BusPublisher


@inject
class LightCreator:
    def __init__(self, light_repository: IlluminationRepository, bus_publisher: BusPublisher):
        self.bus_publisher = bus_publisher
        self.light_repository = light_repository

    def create(self, alias: LightAlias, location: Location) -> Light:
        light = Light.create(alias, location, LightStatus(False))
        self.light_repository.save(light)

        self.bus_publisher.publish(light.pull_events())
        return light
