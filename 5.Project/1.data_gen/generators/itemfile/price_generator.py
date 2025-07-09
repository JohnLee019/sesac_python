import random

class PriceGenerator:
    def identifyPrice(self, type):
        if type == 'Cake':
            price = random.choice(range(5500, 9001, 500))
        else:
            price = random.choice(range(4000, 6501, 500))
        return price
    