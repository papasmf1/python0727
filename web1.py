# web1.py 
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 (HTML, XML)
soup = BeautifulSoup(page, "html.parser")
#로딩한 문서 보기 
#print( soup.prettify() )
#<p> 몽땅 찾기 
#print( soup.find_all("p") )
#<p class=outer-text> :필터링하는 경우
#class는 파이썬의 키워드 class_ 
#print( soup.find_all("p", class_="outer-text") )

#태그 내부의 문자열만 리턴 
for item in soup.find_all("p"):
    #앞뒤에 태그를 없애고 컨텐츠만 가져오기 
    title = item.text.strip() 
    title = title.replace("\n", "")
    print(title)

    


