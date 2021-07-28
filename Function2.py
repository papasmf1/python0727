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

#불변형식을 함수내부에서 읽기+쓰기를 할 경우 맵핑 
g = 1 
def testScope(a):
    #선택한 블럭을 주석처리: ctrl + /, cmd + /  
    # global g 
    # g = 2 
    return a+g

#호출
print( testScope(1) ) 
print("전역변수 g:", g) 

#함수의 기본값 셋팅 
def times(a=10, b=20):
    return a*b 

#호출 
print( times() )
print( times(5) )
print( times(5,6) )

#가변인자 처리(*는 튜플이라는 의미)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAMM") )

#정의되지 않은 인자 처리(**는 옵션으로 딕셔너리로 받기)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출 
print( userURIBuilder("credu.com", "80", id="kim", password="1234"))
print( userURIBuilder("credu.com", "80", id="kim", password="1234",  
    name="mike", age="30"))

