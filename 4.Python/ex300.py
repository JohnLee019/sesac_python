# 7. print("naver", "kakao", "samsung", sep=";")

# 9. print("first", end="");print("second") 

# string = "홀짝홀짝홀짝"
# 23. print(string[::2])    [start:end:step]

# 24. string = "PYTHON"
# print(string[::-1])

# 25. phone_number = "010-1111-2222"
# print(phone_number.replace("-", ""))

# 27. url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])     '.'을 기준으로 index를 줌

#28. string은 수정 불가

# 29. string = 'abcdfe2a354a32a'
# print(string.replace('a', 'A'))

# 40. data = "   삼성전자    "
# print(data.strip())   좌우 공백을 제거  rstrip은 오른쪽 공백 제거

# 45. ticker = "btc_krw"
# print(ticker.endswith('krw')) krw와 같이 뭐로 끝나는지 반대로 startswith도 존재

#47. a = "hello world"
# a.split() splic안에 있는것을 기준으로 문자열로 나눔

# 52. movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)             무엇인가를 추가할 때는 append("추가할거")

# 53. movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")  
# print(movie_rank)                리스트의 `insert(인덱스, 원소)` 반대로 뭐를 삭제할때는 del move_rank[index]

#57, 58, 59
#max([]), minx([]), sum([]), len([]) => 리스트에 있는 데이터의 개수

# 66. interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))             .join은 앞에서 어떻게 할지 쓰는거

# 69. string = "삼성전자/LG전자/Naver"
# interest = string.split('/')
# print(string.split('/'))          split("뭐로") 하면 문자열로 분리되어서 저장

# 70. data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)                     리스트를 오름차순으로 정렬

# 73, 75 튜플에서 하나의 값을 저장시 끝에 , 붙이기
# my_tuple = (1, )  ","로 여러개를 구분 지어서 쓰면 그것은 자동으로 튜플로 인식 t = 1, 2, 3, 4 => 튜플

# 77. interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)
# print(type(data))                 튜플을 리스트로 변환 <=> 반대로는 tuple(list 변수)

#80 data = tuple(range(2, 100, 2))
# print( data )             지정된 시작점, 끝점, 증가 수

#81 scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, b= scores
# print(valid_score)            *을 붙이면 그전까지 다 

# 87. ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)            딕셔너리에 물건 추가 방법

# 88. ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}      
# print("메로나 가격: ", ice["메로나"])       이름이 key-value에서 value가져오기 지우고 싶으면 del

# 94. inventory = {"메로나": [300, 20], 
#              "비비빅": [400, 3], 
#              "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]
# print(inventory)                  디렉토리 추가 방법

# 95. icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(icecream.keys())            키 값만 출력 <=> value 값만 보고 싶으면 values()

# 99. keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)               zip은 key와 value 값들 정렬 그리고 dict()로 캐스팅

# 119. fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가좋아하는계절은: ")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")          in을 사용시 key의 값으로 확인하고 dic에.values()를 쓰면 values의 값으로 확인

# 172. price_list = [32100, 32150, 32000, 32500]
# for i, v in enumerate(price_list):
#     print(i, v)               enumerate => 리스트나 튜플 같은 iterable 순회시 index와 value를 동시에 가져옴


# 241. import datetime

# now = datetime.datetime.now()
# print(now)                    현재 시간을 화면에 출력

import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))