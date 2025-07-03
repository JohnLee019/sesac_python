import random

class StoreNameGenerator:
    def __init__(self, file_path):
        self.names = self.data_from_file(file_path)
    
    def data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
        return data

    def generate_store(self):
        return random.choice(self.names)