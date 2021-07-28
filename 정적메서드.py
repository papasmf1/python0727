# 정적메서드.py
class MyCalc(object):
    #클래스에서 호출하는 정적 메서드 
    @staticmethod
    def my_add(x,y):
        return x+y
    #인스턴스에서 호출하는 인스턴스 메서드
    def methodA(self):
        print("methodA()호출")


#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

#인스턴스를 생성
calc = MyCalc()
calc.methodA() 

