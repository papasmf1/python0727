# DemoDict2.py 

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
#멤버십 테스트 
print( "park" in phone )
print( "moon" not in phone )


#참조를 복사 
p = phone 
p["kang"] = "1234"
print( phone )
print( p )
print( id(phone), id(p) ) 
