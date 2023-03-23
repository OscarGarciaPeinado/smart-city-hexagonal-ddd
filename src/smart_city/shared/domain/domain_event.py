import datetime
import uuid
from uuid import UUID


class DomainEvent:
    event_id: str | UUID
    ts: datetime
    body = {}

    def __init__(self, event_id: str = None, ts: datetime = None):
        self.event_id = event_id if event_id is not None else uuid.uuid4()
        self.ts = ts if ts is not None else datetime.datetime.now()
