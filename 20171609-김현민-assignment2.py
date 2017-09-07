z = 1
x = 0
while x != -1:
    x = int(input("Enter a number:"))
    if x ==-1:
        break
    else:
        for i in range(1, (x + 1)):
            z *= i
    print(z)
    z=1
