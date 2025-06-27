def remove_duplicate(number):
    #구현하기
    # 1. 목록을 순환한다
    # 2. 내가 한번도 본적이 없는 숫자면 반환 리스트에 담는다
    unique_numbers = []
    for num in numbers:
        seen_num = False
        for prev_num in unique_numbers:
            if num == prev_num:
                seen_num = True
        if seen_num == False:
            unique_numbers.append(num)

    return unique_numbers

def remove_duplicate2(number):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


def remove_duplicate3(number):
    return list(set(number))


numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
print(remove_duplicate(numbers))
print(remove_duplicate2(numbers))
print(remove_duplicate3(numbers))