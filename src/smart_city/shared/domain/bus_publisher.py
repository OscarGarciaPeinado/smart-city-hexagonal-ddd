import abc
from abc import ABC
from typing import List

from shared.domain.domain_event import DomainEvent


class BusPublisher(ABC):

    @abc.abstractmethod
    def publish(self, domain_event: List[DomainEvent]) -> None:
        ...
