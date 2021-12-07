n = "강아지"

print (n)

n = "고양이"

print (n)

print('n')

n = 3+7

print (n)

m = "강아지"

print (m)

n *= 5

print(n)

height = 177

print(type(height))

# 형의 변환

h = 177
print ("신장은 " + str(h) + "cm 입니다.")

a = 35.4
b = 10
print (a+b)

h=1.7
w = 60
bmi = w / h **2

#당신의 bmi은 무엇입니다' 라고 출력하기
print ("당신의 bmi는 " + str(bmi) + "입니다")

n = "10"
print (n*3)

# "10"이라는 문자열이 3번 반복되서 출력

print(1+1 ==3)

print (4+6 != -10)

animal = "cat"
if animal == "cat" :
    print ("고양이가 참 귀엽네요.")
    
n = 16
if n > 15 :
    print ("큰 숫자")
    
n = 2
if n == 1:
    print("우승을 축하합니다.")
else :
    print ("아쉽습니다 당신은 " + str(n) + "번째로 도착했습니다.")
    
n = 14
if n > 15 :
    print ("큰 숫자")
else :
    print ("작은 숫자")
    
n = 14
if n>15 :
    print ("큰 숫자")
elif 11<=n<=15 :
    print ("중간 숫자")
else : 
    print ("작은 숫자")
    
n_1 = 14
n_2 = 28

print(n_1>8  and n_1<14)

print(not n_1 ** 2 < n_2*5)

year = 2021

if year % 400 != 0 and year%100 == 0 :
    print(str(year) + "평년입니다")
elif year % 4 == 0 :
    print(str(year) + "윤년입니다.")
else :
    print(str(year) + "평년입니다.")
