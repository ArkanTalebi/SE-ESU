from datetime import datetime

from src.utils.random_id_generator import UniqueIDGenerator
from src.models.enums import DischargeStatus


class Discharge:
    def __init__(self, patient_id: int, discharge_status: DischargeStatus) -> None:
        self.id = UniqueIDGenerator.generate_id()
        self.patient_id = patient_id
        self.discharge_status = discharge_status
        self.discharge_date = datetime.now()

    def __str__(self):
        return (
            f"Discharge ID: {self.id}\n"
            f"Patient ID: {self.patient_id}\n"
            f"Discharge Status: {self.discharge_status.value}\n"
            f"Discharge Date: {self.discharge_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
