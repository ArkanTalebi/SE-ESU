from enum import Enum


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class HealthStatus(Enum):
    ALIVE = 'alive'
    INJURED = 'injured'
    DEAD = 'dead'


class UnitStatus(Enum):
    IDLE = 'idle'
    BUSY = 'busy'


class Location(Enum):
    HOSPITAL = 'hospital'
    STORE = 'store'
    CITY = 'city'
