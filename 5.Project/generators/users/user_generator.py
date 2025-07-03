from name_generator import NameGenerator
from birthdate_generator import BirthdateGenerator
from gender_generator import GenderGenerator
from address_generator import AddressGenerator
from age_generator import AgeCalculate
from id_generator import IdGenerator

class UserGenerator:
    def __init__(self):
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')
        self.age_gen = AgeCalculate()
        self.id_gen = IdGenerator()
        
    def generate_user(self, count):
        users = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            age = self.age_gen.generate_age()
            users.append((id, name, gender, age, bday, address))
        return users
    
class DisplayUsersData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        print("Id,Name,Gender,Age,Birthdate,Address")
        for id, name, gender, age, birthdate, address in data:
            print(f"{id},{name},{gender},{age},{birthdate},{address}")

my_data = DisplayUsersData()
my_data.print_data(10)
