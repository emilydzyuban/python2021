#Інструкції якщо та або якщо
import sys
import math
print("Введіть свій вік")
вік = int(sys.stdin.readline())
if вік == 10:
    print("Привіт")
elif вік == 11:
    print("Скільки буде 2+2?")
    ans = int(sys.stdin.readline())
    if ans == 4:
        print("Правильно")
    else:
        print("Невірно") 
elif вік == 12:
    print("Скільки буде 2*3?") 
    ans2 = int(sys.stdin.readline())
    if ans2 == 6:
        print("Правильно")
    else:
        print("Невірно")
else:        
     print("Error") 
num = 5
num2 = 2 
res = math.ceil(num/num2)
print(res)
res2 = math.floor(num/num2)
print(res2)
print("Надайте довжину в сантиметрах")
len2 = int(sys.stdin.readline())
metr = math.floor(len2/100)
print("Кількість повних метрів = ",metr)
metr2 = math.ceil(len2/100)
print("Кількість повних метрів = ",metr2)





















 


