numbers = [3, 7, 2, 9, 1, 4, 5, 8, 6]

def find_max(numbers):
    #위 목록에서 가장 큰 수를 반환하시오
    #for 와 if 를 사용해서...
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

print(find_max(numbers))
