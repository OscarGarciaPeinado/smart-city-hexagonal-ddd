import copy
import uuid

from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.light_id import LightId
from illumination.domain.entity.light_status import LightStatus
from illumination.domain.entity.location import Location
from illumination.domain.events.light_created_event import LightCreatedEvent
from shared.domain.aggregate_root import AggregateRoot


class Light(AggregateRoot):

    def __init__(self, light_id: LightId, alias: LightAlias, location: Location,
                 status: LightStatus):
        self.alias = alias
        self.status = status
        self.location = location
        self.light_id = light_id

    def get_alias(self) -> LightAlias:
        return self.alias

    def turn(self):
        self.status.turn()
        self.status = copy.deepcopy(self.status)

    @staticmethod
    def create(alias: LightAlias, location: Location, status: LightStatus):
        light_id = LightId(str(uuid.uuid1()))
        light = Light(light_id, alias, location, status)

        light_created_event = LightCreatedEvent(light.light_id, light.alias, light.location,
                                                light.status)
        light.push_event(light_created_event)
        return light
