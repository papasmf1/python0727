# DemoStr.py 
#반복적인 문자열 생성
names = ["전우치","이순신","박문수"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("=" * 40)


#문자열 형식의 메서드(string ---> str)
print( dir(str) )

#실제 사용하는 문자열 처리 메서드 
strA = "<<<  spam and ham  >>>"
print(strA)
#삭제할 문자를 지정
result = strA.strip("<> ")
print(result)
print( len(result) ) 
result2 = result.replace("spam", "spam and egg")
print(result2)
lst = result2.split() 
print("리스트:", lst)
result3 = ":)".join(lst)
print("병합한 문자열:", result3)
print("python is powerful".capitalize() )
print("python is powerful".count("p") ) 
print("python is powerful".count("p", 7) )

#정규 표현식
import re 
#정규표현식의 패턴과 매칭이 되면 매칭 객체가 리턴
#match는 정확하게 일치
print( bool(re.match("[0-9]*th", "35th")) )
#패턴을 포함하고 있으면 검색(일반적인 검색) 
print( bool(re.search("[0-9]*th", "35th")) )
print("---함정---")
print( bool(re.match("[0-9]*th", "  35th")) )
#패턴을 포함하고 있으면 검색(일반적인 검색) 
print( bool(re.search("[0-9]*th", "  35th")) )










