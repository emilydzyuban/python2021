import sys
#Цикли while for
for x in range(0,5):
    print("Hi!")
num = [1,2,3,4,5]
for i in num:
    print(i)
print("Надайте ціле число")
n = int(sys.stdin.readline())#12
number = list(range(0, n, 2))# 0 2 4 6 8 10 sum = 30
sum2 = 0
mult = 1
for k in number: 
    sum2 = sum2+k
    mult = mult * k                              # 0 + 0 = 0
print("Сума елементів списку", sum2)             # 0 + 2 = 2
print("Добуток елементів списку", mult )         # 2 + 4 = 6
                                                 # 6 + 6 = 12
                                                 # 12 + 8 = 20
                                                 # 20 + 10 = 30
for j in range(0,20):
   print("hello")
   if j > 8:
       break;
print("Надайте перше число")
a = int(sys.stdin.readline())
print("Надайте друге число")
b = int(sys.stdin.readline())
count = 0
for r in range(a,b):
    count += 1
