from generators.orderItem.id_generator import OrderitemIdGenerator
from generators.itemfile.id_generator import IdGenerator
from generators.orderfile.id_generator import OrderIdGenerator

class OrderItemGenerator:
    def __init__(self):
        self.id_gen = OrderitemIdGenerator()
        self.item_id_gen = IdGenerator()
        self.order_id_gen = OrderIdGenerator()
    
    def generate_orderItem(self, count):
        orderItems = []
        for _ in range(count):
            order_item_id = self.id_gen.generate_id()
            item_id = self.item_id_gen.generate_id()
            order_id = self.order_id_gen.generate_id()
            orderItems.append((order_item_id, item_id, order_id))
        return orderItems
    
class DisplayOrderItems(OrderItemGenerator):
    def print_data(self, count):
        data = self.generate_orderItem(count)
        print("Id,OrderId,Itemid")
        for order_item_id, item_id, order_id in data:
            print(f"{order_item_id}, {item_id}, {order_id}")

my_data = DisplayOrderItems()
my_data.print_data(10)