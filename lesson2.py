import sys
number = 15
number2 = 18
my_name ="Emma"
#Арифметичні дії + - * / - ділення % - остача від ділення
result = number * number2
print(result)
a = 5
b = 3
res = a**b
print(res)
print("Ця програма вміє обчислювати площу та периметр прямокутника")
print("Введіть довжину першої сторони")
сторона_прямокутника_1 = int(sys.stdin.readline())
print("Введіть довжину другої сторони")
сторона_прямокутника_2 = int(sys.stdin.readline())
S = сторона_прямокутника_1 * сторона_прямокутника_2
P = 2 * (сторона_прямокутника_1 + сторона_прямокутника_2)
print("Площа прямокутника = ", S)
print("Периметер прямокутника = ", P)
print("Ця задача рахує середнє арифметичне двох чисел")
num1 = 35
num2 = 73
res = (num1 + num2)/2
print("Середнє арифметичне = ", res)
#Умовні інструкції if
print("Надайте число")
num5 = int(sys.stdin.readline()) 
if num5 > 10:
    t = num5+7
    print(t)
else:
    r = num5 * 7
    print(r)
#Розгляньмо символи що можуть входити до складу умов
    # == - перевіряє рівність чисел
print("Надайте перше число")    
p = int(sys.stdin.readline())     
print("Надайте друге число")
k = int(sys.stdin.readline())
print("Перевірка на рівність")
if p == k:
    print("Числа рівні між собою")
else:
    print("Числа нерівні між собою")
    # != - перевірка на нерівність
    # >= - більше або дорінює
    # <= - менше або дорівнює
вік = 10
if вік >=10:
    print("Привіт друже!")
else:
    print("Ти ще замалий!")
