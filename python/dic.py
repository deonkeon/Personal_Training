town = {"경기도" : "수원", "서울" : "중구"}

print(town)

print (type(town))

print(town["경기도"])

print("경기도의 중심 도시는 " + town["경기도"] + "입니다.")

print ("서울의 중심 도시는 " + town["서울"] + "입니다.")

town["제주시"] = "제주도"
town["경기도"] = "분당"

print(town)

del town["경기도"]

print(town)

x = 5
while x != 0:
    print(x-1)
    x -= 1
    
x = 5
while x != 0:
    x -= 1
    print (x)
    
x = 5
while x != 0:
    x -= 1
    if x != 0:
        print(x)
    else :
        print("Bang")
        
storages = [1,2,3,4]
for number in storages:
    print (number)
    
    
storages = [1,2,3,4,5,6]
for n in storages:
    print(n)
    if n == 4 :
        print("끝")
        break;
    
for n in storages :
    if n%2==0:
        continue
        print(n)
