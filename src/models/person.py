from datetime import datetime

from src.models.base import BaseEntity
from src.models.enums import Gender, HealthStatus, Location
from src.utils.random_id_generator import RandomIDGenerator


class Patient(BaseEntity):
    def __init__(self, name: str, gender: Gender, birth_date: datetime, health_status: HealthStatus, location: Location):
        super().__init__()
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.health_status = health_status
        self.location = location

    @classmethod
    def from_dict(cls, data):
        if data['status'].value == HealthStatus.ALIVE.value:
            health_status = HealthStatus.ALIVE
        elif data['status'].value == HealthStatus.INJURED.value:
            health_status = HealthStatus.INJURED
        else:
            health_status = HealthStatus.DEAD

        if Location.CITY.value in data['current_entity'].value:
            location = Location.CITY.value
        elif Location.STORE.value in data['current_entity'].value:
            location = Location.STORE.value
        else:
            location = ""

        return cls(data['name'], data['gender'], data['birth_date'], health_status, data['current_entity'], location)

    def __str__(self) -> str:
        return (f"Patient ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Gender: {self.gender.value}\n"
                f"Birth Date: {self.birth_date.strftime('%Y-%m-%d')}\n"
                f"Health Status: {self.health_status.value}\n"
                f"Location: {self.location.value}")
