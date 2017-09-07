num = int(input("Enter a number : "))
a = 1
if num < 0:
    print()
else:
    for i in range(1, num + 1):
        a = a * i
    print(num,'! =',a)
