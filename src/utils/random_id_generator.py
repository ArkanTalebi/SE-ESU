import uuid


class RandomIDGenerator:
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
