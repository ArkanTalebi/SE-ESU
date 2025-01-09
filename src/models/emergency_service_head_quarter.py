from copy import deepcopy
import requests

from src.models.base import BaseEntity
from src.models.snapshot import Snapshot
from src.models.person import Patient
from src.models.unit import Unit


class EmergencyServiceHeadQuarter(BaseEntity):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.units: dict[int, Unit] = self.__initialize_units()
        self.available_units: dict[int, Unit] = self.units
        self.max_capacity = len(self.units)
        self.patient_in_queue = dict[int, Patient]
        self.patient_in_service = dict[int, Patient]
        self.snapshots: dict[int,
                             Snapshot] = self.__initialize_initial_snapshot()
        self.__last_snapshot = self.snapshots

    def register(self, url) -> None:
        response = requests.post(
            url,
            json={
                "entity_type": EmergencyServiceHeadQuarter.__name__,
                "max_capacity": self.max_capacity,
                "eav": {
                    "units": self.units,
                    "creation_date": self.creation_date,
                    "modified_date": self.modified_date
                }
            }
        )

        body = response.json()
        self.entity_id = body['entity_id']
        self.time_rate = body['time_rate']

    def take_snapshot(self, url) -> None:
        response = requests.get(url, params={"entity_id": self.entity_id})

        snapshot = Snapshot.from_dict(response.json())
        self.snapshots[snapshot.id] = snapshot
        self.__last_snapshot = snapshot

    def accept_person(self, url) -> bool:
        return requests.post(url, json={"entity_id": self.entity_id, "persons_id": self.__admit_process()}).json()

    def __admit_process(self) -> list:
        patients: dict[int, Patient] = deepcopy(self.patient_in_queue)
        for person in self.__last_snapshot.persons:
            patient = Patient.from_dict(person)
            patients[patient.id] = patient

        locations_with_patient = dict[str, list]  # List of Patient
        for patient in patients.values():
            if locations_with_patient.get(patient.location):
                locations_with_patient[patient.location].append(patient)
            else:
                locations_with_patient[patient.location] = [patient]

        maximum = max(locations_with_patient, key=lambda loc: len(locations_with_patient[loc]))
        for unit_id, unit in self.units.items():
            if unit.status == UnitStatus.IDLE:
                unit.status = UnitStatus.ASSIGNED  # Change status to ASSIGNED
                assigned_unit_id = unit_id
                print(f"Assigned {unit.name} to location: {max_location}")
                break
            else:   
                print("No IDLE units available.")
                return []  # Return empty list if no units are available

        # Return the list of assigned unit IDs (in this case, one unit)
        return [assigned_unit_id]

        

    def __initialize_initial_snapshot(self) -> Snapshot:
        return Snapshot(0, [], False)

    def __initialize_units(self) -> None:
        return [Unit(name="Ambulance A", max_capacity=4, vehicle_speed=120),
                Unit(name="Ambulance B", max_capacity=3, vehicle_speed=110),
                Unit(name="Ambulance C", max_capacity=5, vehicle_speed=100),
                Unit(name="Ambulance D", max_capacity=4, vehicle_speed=115)]

    def load_patient(self):
        pass

    def unload_patient(self):
        pass
