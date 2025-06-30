#무작위 숫자 만들기
import random

# print("랜덤 숫자: ", random.randint(1, 100)) 1부터 100까지의 양수를 다 포함하는 랜덤 숫자를 생성

#주사위 던지기 구현
#이 주사위를 100번 던져보고, 1000도 해보고, 10000번도 던져서... 각 숫자가 나올 확율을 출력해보시오
# def roll_dice(input):
#     num1 = 0
#     num2 = 0
#     num3 = 0
#     num4 = 0
#     num5 = 0
#     num6 = 0
#     for i in range(1, input +1):
#         result = random.randint(1,6)
#         if result == 1:
#             num1 += 1
#         if result == 2:
#             num2 += 1
#         if result == 3:
#             num3 += 1
#         if result == 4:
#             num4 += 1
#         if result == 5:
#             num5 += 1
#         if result == 6:
#             num6 += 1
#     print(f"1이 나온 횟수: {num1}번, 확율: {num1 / input}")
#     print(f"2이 나온 횟수: {num2}번, 확율: {num2 / input}")
#     print(f"3이 나온 횟수: {num3}번, 확율: {num3 / input}")
#     print(f"4이 나온 횟수: {num4}번, 확율: {num4 / input}")
#     print(f"5이 나온 횟수: {num5}번, 확율: {num5 / input}")
#     print(f"6이 나온 횟수: {num6}번, 확율: {num6 / input}")

# roll_dice(10000)
counts =[0,0,0,0,0,0]
def roll_dice(numbers):
    for i in range(numbers):
        result = roll_dice()
        counts[result -1] += 1
roll_dice(10)
for i in range(6):
    print(f"{i+1}이 나온 횟수: {counts[i]}: 확율: {counts[i] / sum(counts)}")

count2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
