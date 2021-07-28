# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 메서드 
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수(클래스에 내부에 멤버변수를 숨김) 
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금을 처리 
    def deposit(self, amount):
        self.__balance += amount 
    #출금을 처리 
    def withdraw(self, amount):
        self.__balance -= amount
    #사용자가 요구하는 문자열을 정의 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#에러 상황
#print(account1.__balance)
#백도어(테스트용도)
print(account1._BankAccount__balance) 




