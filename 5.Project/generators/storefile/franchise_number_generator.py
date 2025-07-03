import random
from smallCity_generate import smallCityGenerator
from name_generator import StoreNameGenerator
    
class NameNumGenerator:
    def __init__(self):
        self.district_gen = smallCityGenerator('city_smaller.txt')

    def generate_storeName(self, storeName):
        fullName = f"{storeName} {self.district_gen.generate_district()}{str(random.randint(1, 5))}호점" 
        return fullName