# Function3.py

#람다 함수 정의
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )
#정의하고 바로 호출
print( (lambda x:x*x)(3) ) 

print( globals() )

#pass 키워드(준비가 되어 있지 않으니 스킵)
class Test:
    pass 

#문서화 작업
def add(a,b):
    """이 함수는 2개의 숫자를 
    입력 받아서 덧셈을 실행합니다."""
    return a+b 

#문서를 호출
print( help(add) )




