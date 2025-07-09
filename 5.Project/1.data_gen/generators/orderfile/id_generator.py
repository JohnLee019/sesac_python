import uuid

class OrderIdGenerator:
    def generate_id(self):
        user_id = str(uuid.uuid4())
        return user_id