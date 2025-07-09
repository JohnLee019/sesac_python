from district_generator import DistrictGenerator
from id_generator import IdGenerator
from location_generator import LocationGenerator
from name_generator import StoreNameGenerator
from franchise_number_generator import NameNumGenerator

class StoreGenerator:
    def __init__(self):
        self.storeName_gen = StoreNameGenerator('coffeeStore.txt')
        self.franchiseNum_gen = NameNumGenerator()
        self.district_gen = DistrictGenerator('district.txt')
        self.id_gen = IdGenerator()
        self.location_generate = LocationGenerator('cities.txt')

    def generate_store(self, count):
        stores = []
        for _ in range(count):
            storeName = self.storeName_gen.generate_store()
            id = self.id_gen.generate_id()
            location = self.location_generate.generate_address()
            franchiseNum = self.franchiseNum_gen.generate_storeName(storeName)
            stores.append((id, franchiseNum, storeName, location))
        return stores
    
class DisplayStores(StoreGenerator):
    def print_data(self, count):
        data = self.generate_store(count)
        print("Id,Name,Type,Address")
        for id, franchisenum, storeName, location in data:
            print(f"{id},{franchisenum},{storeName},{location}")

my_data = DisplayStores()
my_data.print_data(10)