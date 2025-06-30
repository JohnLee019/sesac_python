#구(legacy) 언어 방식은??
# if 문으로 다 비교해서.. 나눗셈이 0이면 안되고.. 등등등...

#신(modern) 언어의 방식은??
#try-catch, try-except 이런 형태로 변경해서 오류를 처리

# 이때 try 안에 오는 범위를 최소화 시킬수록 좋은것
# except 내에서 퉁~ 쳐서 하나로 잡지말고, 구체적으로 잡아서 핸들링 할수록 좋은것
try:
    result  = 10 / 0 #crash가 발생함... 실행이 중단되고 프로그램이 종료되고, 더 이상 다음줄로 실행할수가 없음
    print(result)
except ZeroDivisionError:
    print("0으로 나룰 수 없습니다")

#글자를 숫자로 바꾸기 
#다른 모든 언어는 함수의 설명을, 그 함수 위에 씀
def convert_to_int(num_str):
    """글자를 숫자로 바꾸는 함수임

    Args:
        num_str (string): 사용자 입력의 문자열 형태의 숫자로 받음
    
    Returns: 
        result: 변환된 숫자값. 변환에 실패한 경우 None을 반환함
    """
    try:
        result = int(num_str)
    except ValueError:
        print("입력한 값이 숫자가 안입니다. 입력값: ", num_str)
        result = None
    return result

def double_number(num):
    return num * 2

user_input = "10a"
result = convert_to_int(user_input)
if result:
    result = double_number()
    print(f"입력한 숫자: {user_input}의 두배값은 {result}입니다.")
else:
    print("숫자 변환 실패")