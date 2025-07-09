import random

class TimeDateGenerator:
    def generateTimeDate(self):
        month = random.randint(1,12)
        day = random.randint(1, 28)
        hours = random.randint(0,23)
        minutes = random.randint(0,59)
        seconds = random.randint(0,59)
        return f"2025-{month:02d}-{day:02d} {hours:02d}:{minutes:02d}:{seconds:02d}"