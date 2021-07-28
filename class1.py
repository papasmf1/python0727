# class1.py
#클래스를 정의
class Person:
    #초기화 메서드(인스턴스 멤버 변수 초기화 담당)
    def __init__(self):
        self.name = "Default name"
    #일반 인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))


#인스턴스 생성
p1 = Person()
p2 = Person() 
p2.name = "전우치"
p1.print() 
p2.print() 

