# class2.py
#클래스를 정의
class Person:
    #클래스에 소속된 멤버변수(주로 데이터를 공유하는 것이 목적)
    num_person = 0 
    #초기화 메서드(인스턴스 멤버 변수 초기화 담당)
    def __init__(self):
        self.name = "Default name"
        Person.num_person += 1 
    #일반 인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))


#인스턴스 생성
p1 = Person()
p2 = Person() 
p3 = Person() 
print("인스턴스의 갯수:", Person.num_person)





