from id_generator import IdGenerator
from type_generator import TypeGenerator
from price_generator import PriceGenerator
from itemName_generator import ItemNameGenerator

class ItemGenerate:
    def __init__(self):
        self.id_gen = IdGenerator()
        self.type_gen = TypeGenerator()
        self.price_gen = PriceGenerator()
        self.itemName_gen = ItemNameGenerator('items.txt')
    
    def generate_items(self, count):
        items = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            itemName = self.itemName_gen.generate_items_name()
            type = self.type_gen.typeIdentity(itemName)
            price = self.price_gen.identifyPrice(type)
            items.append((id, itemName, type, price))
        return items

class DisplayItems(ItemGenerate):
    def print_data(self, count):
        data = self.generate_items(count)
        print("Id,Name,Type,Price")
        for id, itemName, type, price in data:
            print(f"{id},{itemName},{type},{price}")

my_data = DisplayItems()
my_data.print_data(10)
