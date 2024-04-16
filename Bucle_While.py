num = int(input("Escribe un número entero: "))
print("Tu número fue:" + str(num))
while num != 1:
    print(num, end=",")
    num = num -1
    if num%2==0:
        print(num//2)
    else:
        print(num*3//1)