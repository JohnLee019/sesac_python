import sys
from users.csv_console import DisplayData as UserDisplayData
from storefile.csv_console import DisplayData as StoreDisplayData
from itemfile.csv_console import DisplayData as ItemDisplayData
from orderfile.csv_generator import DisplayData as OrderDisplayData
from orderItem.csv_generator import DisplayData as OrderItemDisplayData

def main():
    # data_type =

    if data_type == 'user':
        my_data = UserDisplayData()
    elif data_type == 'store':
        my_data = StoreDisplayData()
    elif data_type == 'item':
        my_data = ItemDisplayData()
    elif data_type == 'order':
        my_data = OrderDisplayData()
    elif data_type == 'orderItem':
        my_data = OrderItemDisplayData()
    else:
        print("지원되지 않는 data_type 입니다.")
        sys.exit(1)

    if output_format == 'console':
        my_data.print_console(num_data)
    elif output_format == 'csv':
        my_data.print_csv(num_data)
    else:
        print("지원되지 않는 출력 형태입니다.")

if __name__ == "__main__":
    main()