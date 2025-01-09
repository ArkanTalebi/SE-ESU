from datetime import datetime

from src.utils.random_id_generator import RandomIDGenerator


class BaseEntity:
    def __init__(self):
        self.id = RandomIDGenerator.generate_uuid()
        self.creation_date = datetime.now()
        self.modified_date = self.creation_date
