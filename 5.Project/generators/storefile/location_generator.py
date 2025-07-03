import random
from district_generator import DistrictGenerator

class LocationGenerator:
    def __init__(self, file_path):
        self.cities = self.load_data_from_file(file_path)
        self.district_gen = DistrictGenerator('district.txt')

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data
    
    def generate_address(self):
        city = random.choice(self.cities)
        street_num_first = random.randint(1, 60)
        street_num_back = str(random.randint(1, 100))
        if 1 <= street_num_first and street_num_first < 10:
            street_name = str(street_num_first) + '가'
        elif 10 <= street_num_first and street_num_first < 30:
            street_name = str(street_num_first) + '길' 
        else:
            street_name = str(street_num_first) + '로' 
        return f"{city} {self.district_gen.generate_district()} {street_name} {street_num_back}"
