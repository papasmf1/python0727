# web2.py 
#크롤링을 위한 선언 
from bs4 import BeautifulSoup
#웹서버와 통신를 위한 선언 
import urllib.request

#웹서버에 특정 페이지 실행을 요청 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

# 블럭: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
#리스트형식으로 리턴됨: find_all은 해당 태그를 전부 검색합니다. 
cartoons = soup.find_all("td", class_="title")
#find()메서드는 하나라도 검색이 되면 바로 종료합니다. 
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

print("갯수:", len(cartoons) )
#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find("a").text 
    link = item.find("a")["href"]
    print( title.strip() )
    print( link.strip() )
    f.write(title + "\n")

f.close()


