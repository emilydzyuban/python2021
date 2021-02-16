#Списки - зберігають набір або послідовність елементів
numbers = [1,2,3,4,5]
print(numbers)
#Нумерація елементів у списку починається з 0
print(numbers[2])
print(numbers[4])
print(numbers[-1])
print(numbers[-2])
#num [5,5,5,5,5,5]
num = [5]*6   # Список має 6 елементів і усі дорівнюють 5
print(num)
print(numbers[1:4])
numbers[2] = 7
print(numbers)
слова = ['pig']
print(слова)
числа_та_слова = [7,'pig']
print(числа_та_слова)
my_list = [numbers,num,слова,числа_та_слова]
print(my_list)
#range(end) - створює набір чисел від 0 до числа end
n2 = list(range(16))
print(n2)
#range(stast,end) - створює набір чисел від 0 до числа end
n3 = list(range(2,10))
print(n3)
n4 = list(range(10,0,-2))
print(n4)
n5 = list(range(0,10,2))
print(n5)
print(len(n5))
num1 = [1,5,7,6,5,2,9,5,12]
num1.append(9)
print(num1)
num1.insert(2,10)
print(num1)
print(num1.count(5))
num1.pop(3)
print(num1)
a = min(num1)
b = max(num1)
print("Мінімальний елемент списку дорівнює = ",a)
print("Максимальний елемент списку дорівнює = ",b)
comp = ["Microsoft","Gogle","Oracle","Apple"]
item = "Oracle" 
if item in comp:
    comp.remove(item)
print(comp)
















































































































































































