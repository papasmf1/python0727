# DemoFile.py 
url = "http://www.credu.com/?page=" + str(1)  
print(url)

#파일 쓰기 
f = open("c:\\work\\demo.txt", "wt")
f.write("한글\nabcd\n1234\n")
f.close() 

#파일 읽기
f = open("c:/work/demo.txt", "rt")
#전체를 하나의 문자열 변수로 읽기
result = f.read() 
print(result)
#어디쯤 읽기? 
print(f.tell())
#다시 처음으로 돌아가(리셋)
f.seek(0)
print( f.readline() )
print( f.readline() )
#다시 처음으로 
f.seek(0)
lst = f.readlines()
print("lst:", lst) 
for item in lst:
    #치환(패턴, 변경)
    print(item.replace("\n", "")) 

#안전하게 작업을 종료 
f.close() 

#기존 파일에 첨부 
f = open("c:\\work\\demo.txt", "a+")
f.write("새로운 데이터\n")
f.close() 


