from typing import List


class AggregateRoot:
    domain_events = []

    def pull_events(self) -> List:
        events = self.domain_events
        self.domain_events = []
        return events

    def push_event(self, event):
        self.domain_events.append(event)
