from kink import di

from illumination.application.create.light_creator import LightCreator
from illumination.application.turn.turn_light import TurnLight
from illumination.domain.illumination_repository import IlluminationRepository
from illumination.infraestructure.in_memory_illumination_repository import \
    InMemoryIlluminationRepository
from shared.infraestructure.rabbit_mq_bus_publisher import RabbitMqBusPublisher


def bootstrap_di() -> None:
    illumination_repository = InMemoryIlluminationRepository()

    di[IlluminationRepository] = illumination_repository
    di[LightCreator] = LightCreator(light_repository=illumination_repository,
                                    bus_publisher=RabbitMqBusPublisher())
    di[TurnLight] = TurnLight(illumination_repository=illumination_repository)
