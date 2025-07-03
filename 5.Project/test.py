import random
from datetime import datetime
import uuid

class NameGenerator:
    # def __init__(self):
        # self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        # 기존 하드코딩 되어 있던걸, 파일을 통해서 읽는 방식으로 변경해보기
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data

    def generate_name(self):
        return random.choice(self.names)
    
class BirthdateGenerator:
    def generate_birthdate(self):
        year = random.randint(1940, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

class AgeCalculate:
    def generate_age(self):
        birthdate = int(BirthdateGenerator.generate_birthdate(self).split('-')[0])
        age = datetime.now().year - birthdate
        return age

class GenderGenerator:
    def generate_gender(self):
        return random.choice(['Male', 'Female'])
class IdGenerator:
    def generate_id(self):
        user_id = str(uuid.uuid4())
        return user_id
    
class AddressGenerator:
    # def __init__(self):
        # self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
        
    def __init__(self, file_path):
        self.cities = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data
        
    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1, 100)
        return f"{street_num} {city}"

class UserGenerator:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.age_gen = AgeCalculate()
        self.address_gen = AddressGenerator('cities.txt')
        
    def generate_user(self, count):
        users = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            age = self.age_gen.generate_age()
            address = self.address_gen.generate_address()
            users.append((id, name, gender, age, bday, address))
        return users

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        print("Id,Name,Gender,Age,Birthdate,Address")
        for id, name, gender, age, birthdate, address in data:
            print(f"{id},{name},{gender},{age},{birthdate},{address}")

# 최종 실행
my_data = DisplayData()
my_data.print_data(10)