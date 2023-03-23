from illumination.domain.entity.light_alias import LightAlias
from illumination.domain.entity.light_id import LightId
from illumination.domain.entity.light_status import LightStatus
from illumination.domain.entity.location import Location
from shared.domain.domain_event import DomainEvent


class LightCreatedEvent(DomainEvent):

    def __init__(self, light_id: LightId, alias: LightAlias, location: Location,
                 status: LightStatus):
        super().__init__()
        self.alias = alias
        self.status = status
        self.location = location
        self.light_id = light_id

    @staticmethod
    def create(light_id: LightId, alias: LightAlias, location: Location,
               status: LightStatus):
        return LightCreatedEvent(light_id, alias, location, status)
