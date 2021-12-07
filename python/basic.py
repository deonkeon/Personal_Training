c = ['red', 'blue', 'yellow']

print(c)

print (type(c))

n=3

print (['사과,', 'n', '고릴라'])

apple = 4
grape = 3
banana = 6

fruits = [apple, grape, banana]

print(fruits)

fruits_name_1 = "사과"
fruits_num_1 = 2
fruits_name_2 = "귤"
fruits_num_2 = 10

fruits = [[fruits_name_1, fruits_num_1],[fruits_name_2, fruits_num_2]]

print(fruits)

fruits = ["apple", 2, "orange", 4, "grape", 3 , "banana", 1]

print(fruits[1])
print(fruits[-1])

chaos = ["cat", "apple", 2, "orange", 4, "grape", 3, "banana", 1, "elephant", "dog"]

fruits = chaos[1:-2]

print(fruits)

c = ["dog", "blue", "yellow"]

c[0] = "red"
c += ["green"]

print(c)

del c[0]

print(c)

# list var 변수 복사

c = ["red", "blue", "yellow"]

c_copy = c[:]

c_copy[1] = "green"

print(c)
