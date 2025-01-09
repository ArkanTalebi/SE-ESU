from src.models.base import BaseEntity
from datetime import datetime


class Snapshot(BaseEntity):
    def __init__(self, entity_id: int, persons: list, earthquake_status: bool) -> None:
        self.entity_id = entity_id
        self.persons = persons
        self.earthquake_status = earthquake_status

    @classmethod
    def from_dict(cls, data):
        return cls(data['entity_id'], data['persons'], data['earthquake_status'])

    def __str__(self):
        pass
