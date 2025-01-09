from src.models.base import BaseEntity
from src.models.enums import UnitStatus
from src.models.person import Patient


class Unit(BaseEntity):
    def __init__(self, name: str, max_capacity: int, vehicle_speed: int) -> None:
        super().__init__()
        self.name = name
        self.max_capacity = max_capacity
        self.vehicle_speed = vehicle_speed
        self.status = UnitStatus.IDLE
        self.used_capacity = 0
        self.patient = dict[int, Patient]

    def assign_patient(self, patient: Patient) -> None:
        self.patient[patient.id] = patient

    def transfer_to_patients(self):
        self.trasnfer_to_patients_duration = self.__estimate_trasfer_to_patients_duration() / \
            self.vehicle_speed

    def transfer_to_hospital(self):
        self.trasnfer_to_hospital_duration = self.__estimate_trasfer_to_hospital_duration() / \
            self.vehicle_speed

    def __estimate_trasfer_to_patients_duration(self) -> int:
        pass

    def __estimate_trasfer_to_hospital_duration(self) -> int:
        pass

    def __str__(self) -> None:
        return f"Unit(max_capacity={self.max_capacity}, vehicle_speed={self.vehicle_speed}, used_capacity={self.used_capacity})"
