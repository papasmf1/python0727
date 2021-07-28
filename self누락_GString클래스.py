#전역변수(이름 충돌을 경험하는 경우) 
str = "Not Class Member"

#파이썬은 모호한 것 보다는 명시적인 것이 좋다~~ 
class GString:
    #초기화 메서드(인스턴스 멤버 변수를 초기화)
    #self는 키워드는 아니지만 자리가 예약되어 있다~ 
    def __init__(self):
        #인스턴스에서 사용하는 멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 실수 
        print(self.str)

g = GString()
g.set("First Message")
g.print()
