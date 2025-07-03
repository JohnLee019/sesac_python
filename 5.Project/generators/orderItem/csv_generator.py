import sys
import csv
from generators.orderItem.orderItem_generator import OrderItemGenerator

class DisplayData(OrderItemGenerator):
    def print_console(self, count):
        data = self.generate_orderItem(count)
        for order_item_id, item_id, order_id in data:
            print(f"Id: {order_item_id}\nOrderId: {item_id}\nItemId: {order_id}\n")

    def print_csv(self, count):
        data = self.generate_orderItem(count)
        with open('ordersItem.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # CSV 헤더 작성
            writer.writerow(['order_item_id', 'item_id', 'order_id'])
            # 각 행에 사용자 데이터 작성
            for order_item_id, item_id, order_id in data:
                writer.writerow([order_item_id, item_id, order_id])
        print("CSV 파일에 저장 완료")

if len(sys.argv) > 1: 
    num_data = int(sys.argv[1])
else:
    num_data = int(input("원하는 데이터 갯수를 입력하시오: "))

output_format = 'console'
if len(sys.argv) > 2:
    output_format = sys.argv[2]

my_data = DisplayData()
if output_format == 'console':
    my_data.print_console(num_data)
elif output_format == 'csv':
    my_data.print_csv(num_data)
else:
    print("지원되지 않는 출력 형태입니다.")

