# DemoLoop2.py 
# 디버깅 셋팅(논리적인 오류 찾기)

lst = ["apple", 100, 3.14]
#중단점(Break Point)
for item in lst:
    print(item, type(item))

#구구단(반복구분이 중첩)
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


#반복구문에서 break, continue구문 연습 

lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5: 
        break 
    print("Item:{0}".format(item))


print("---continue구문---")
for item in lst:
    if item % 2 == 1: 
        continue
    print("Item:{0}".format(item))

#수열함수를 사용 
print( range(10) )
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(2000, 2022)) )

#for루프를 사용할 수 있나요? 
print("----수동반복----")
for x in range(10):
    print(x)











