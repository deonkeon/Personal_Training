animals = ["tiger", "dog", "elephant"]

# 정수형의 인덱스와 리스트에 포함된 밸류값 출력

# 인덱스 정수형과 자료형을 한쌍씩으로 해서 출력

for index,value in enumerate(animals) :
    print("index:" + str(index),value)
    
fruits = [["strawberry", "red"],["peach", "pink"],["banana", 'yellow']]

for fruit, color in fruits:
    print(fruit + " is " + color)
    
# 딕셔너리의 포문 출력 (루프)   
    
fruits = {"strawberry" : "red", "peach" : "pink", "banana" : "yellow"}
for fruit, color in fruits.items():
    print(fruit + color)
    
# list 요소는 ,로 나열되므로 결과도출시 ( , ) 사용 enumerate는 정수형 0부터 시작하는 인덱스와 자료형 밸류값을 도출

# 리스트 속 리스트는 제일 안의 리스트 요소들의 수만큼 도출변수를 설정시켜줘야함. 위의 예시참조. 리스트 하나씩 묶여서 출력됨

# 딕셔너리 형은 itmes() 함수를 사용

town = {"경기도" : "분당", "서울" : "중구", "제주도" : "제주시"}

for prefecture, captial in town.items():
    print (prefecture, captial)
    
# 상품의 가격과 개수, 지불 금액과 거스름돈을 표시하는 프로그램

items = {"지우개" : [100, 2], "펜" : [200, 3], "노트" : [400, 5]}
# items 딕셔너리형 키 & 밸류
total_price = 0
for item in items:
    print (item + "은(는) 한개에 " +str(items[100][0]) + "원이며, " + str(items[item][1]) + "개 구입합니다. ")
