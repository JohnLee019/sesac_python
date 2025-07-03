from birthdate_generator import BirthdateGenerator
from datetime import datetime

class AgeCalculate:
    def generate_age(self):
        birthdate = int(BirthdateGenerator.generate_birthdate(self).split('-')[0])
        age = datetime.now().year - birthdate
        return age