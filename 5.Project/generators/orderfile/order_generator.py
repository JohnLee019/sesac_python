from generators.users.id_generator import IdGenerator
from generators.storefile.id_generator import IdGenerator
from generators.orderfile.id_generator import OrderIdGenerator
from generators.orderfile.time_date_generator import TimeDateGenerator

class OrderGenerator:
    def __init__(self):
        self.user_id_gen = IdGenerator()
        self.store_id_gen = IdGenerator()
        self.order_id_gen = OrderIdGenerator()
        self.orderAt_gen = TimeDateGenerator()
    def generate_orders(self, count):
        orders = []
        for _ in range(count):
            user_id = self.user_id_gen.generate_id()
            orderAt = self.orderAt_gen.generateTimeDate()
            store_id = self.store_id_gen.generate_id()
            order_id = self.order_id_gen.generate_id()
            orders.append((user_id, orderAt, store_id, order_id))
        return orders
    
class DisplayOrders(OrderGenerator):
    def print_data(self, count):
        data = self.generate_orders(count)
        print("Id,OrderAt,StoreId,UserId")
        for user_id, orederAt, store_id, order_id in data:
            print(f"{user_id},{orederAt},{store_id},{order_id}")
my_data = DisplayOrders()
my_data.print_data(10)