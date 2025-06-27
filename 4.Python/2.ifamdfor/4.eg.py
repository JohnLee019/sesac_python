# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #여기를 순회하면서 짝수만
# for num in numbers:
#     if num % 2 == 0:
#         print(f"숫자 {num} 은 짝수입니다")
#     elif num % 2 != 0:
#         print(f"숫자 {num} 은 홀수입니다")

# def getEvenNumbers(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers
# even = getEvenNumbers(numbers)
# print(f"짝수는:", even)
# print(f"짝수는: {even}")

#다음 목록에서 성적이 A인 학생만 반환하시오
students = {
    '김철수': 70,
    '이영희': 82,
    '박민수': 88,
    '최지은': 75,
    '장현우': 93,
    '서민정': 67,
    '정우성': 99,
    '한지만': 76,
    '오세훈': 61,
    '송지효': 85,
}


#방법 1
def get_a_grade_students(students):
    result = []
    for name, score in students.items():
        if score >= 90:
            result.append(name)
    return result

a_student = get_a_grade_students(students)
print(a_student)

#방법 2

def get_a_grade_students2(students):
    result = []
    for name, score in students.items():
        if get_grade(score) == 'A':
            result.append(name)
    return result

a_student = get_a_grade_students(students)
print(a_student)




def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    return 'F'
# for name, num in students:
#     over_nine = []
#     if num >= 90:
#         over_nine.append(name.values())

# print(f"{over_nine}")
        