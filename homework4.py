import sys
print("Введіть число")
p = int(sys.stdin.readline())
print("Перевірка на відємність числа")
if p >= 0:
    print("Число додатнє")
else:
    print("Число від'ємне. Введіть додатнє число")
    p = int(sys.stdin.readline())
