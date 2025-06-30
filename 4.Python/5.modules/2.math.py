#기본 수학 연산을 하기 위한 빌트인 모듈
import math

print(math.pi)

#원의 넓이를 구할거야
#pi * r^2
radius = 5
area = math.pi * radius **2
area2 = math.pi * math.pow(radius, 2)
print(f"반지름이 {radius}인 원의 넓이는 {area2:6.2f}입니다")

text = "hi"
print(f"[{text:<10}]")
print(f"[{text:>10}]")
print(f"[{text:^10}]")