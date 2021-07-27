# DemoDict.py 
d = dict(a=1, b=2, c=3)
print(d)
print(type(d)) 


color = {"apple":"red", "banana":"yellow"}
print( len(color) )
print( color["apple"] )
#데이터를 추가
color["cherry"] = "red"
print( color )
#데이터를 삭제 
del color["apple"]
print( color )
#반복 구문
for item in color.items():
    print(item)

print("----key, value---")
for k,v in color.items():
    print(k,v)

#장비를 관리한다. 
device = {"아이폰":5, "갤럭시":10, "아이패드":20}
print( device )
#입력 
device["맥프레"] = 15 
print( device )
#수정 
device["아이폰"] = 6 
print( device )
#삭제 
del device["아이폰"]
print( device )












