from typing import List

from shared.domain.bus_publisher import BusPublisher
from shared.domain.domain_event import DomainEvent
import pika


class RabbitMqBusPublisher(BusPublisher):
    QUEUE = "EVENTS_QUEUE"

    def __init__(self):
        credentials = pika.PlainCredentials('USER', 'PASS')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.QUEUE)

    def publish(self, domain_event: List[DomainEvent]) -> None:
        self.channel.basic_publish(exchange="", routing_key=self.QUEUE, body='test'.encode("utf-8"))

        print("Publish")
