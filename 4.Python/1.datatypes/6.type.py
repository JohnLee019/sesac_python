x = 5
y ="hello"
z = [1, 2, 3]

print(type(x))
print(type(y))
print(type(z))

#print(x.upper()) 각각의 변수 타입은 클래스로 만들어져 있고, 그 안에 있는 함수를 통해서 세부 클래스의 함수들이 동작한다.

print(isinstance(x, int)) #x는 int로 만들어진거야?
print(isinstance(x, (int, float))) #x는 int나 float로 만들어진거야?
print(isinstance(y, (str, list))) 
print('-' * 10)
#클래스 A 만들어짐
class A:
    pass #아무것도 안해도됨 => 빈 클래스 생성
class B(A): #B extends A (A를 상속받았음)
    pass
class C:
    pass

b = B() #b = new B(), b라는 변수를 b라는 클래스로 찍어냄

print(isinstance(b, A)) #true
print(isinstance(b, B)) #true
print(isinstance(b, C)) #false

a = A()
print(isinstance(a, A)) #true
print(isinstance(a, B)) #false
print(isinstance(a, C)) #false


