# Function1.py 
#함수를 정의
def times(a,b):
    return a*b 

#함수를 호출 
print( times(3,4) )

#함수를 값을 리턴하는 경우도 있고 아닌 경우도 있다. 
def setValue(newValue):
    x = newValue
    print("내부:", x)

#호출 
result = setValue(5)
print(result)

def swap(x,y):
    return y,x 

#호출 
result = swap(5,6)
print(result)

#디버깅 연습을 위한 교집합 함수 
def intersect(prelist, postlist):
    #지역변수:교집합 문자를 저장 
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에도 있고 아직 retList에 없으면 
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#호출
print( intersect("HAM", "SPAM") )


