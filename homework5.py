import sys
while(1==1):
    print("Надайте двухзначне число")
    number = int(sys.stdin.readline())
    value = str(number)
    print(f"Ви ввели {value}")
    if len(value)==2:
        print(f"Ваш результат {value[1]}{value[0]}")
        break
    else:
        print("Ви ввели не двохзначне число")
