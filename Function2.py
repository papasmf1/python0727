# Function2.py 

#변경이 불가능한 형식
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

#변경이 가능한 형식(99%)
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#Pass By Reference 
def change(x):
    #복사본을 사용하도록 수정
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

#변수의 이름을 해석하는 순서(LGB)
#전역변수(함수 외부)
x = 5 
def func1(a):
    return a+x 

#호출
print( func1(1) )

def func2(a):
    #지역변수(함수 내부에서 초기화)
    x = 2 
    return a+x 

#호출
print( func2(1) )
