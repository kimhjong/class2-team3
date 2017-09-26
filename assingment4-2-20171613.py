def con(n,m):  
    if m == 1:
        return n
    elif m <= 0:
        return 0
    elif n == m:
        return 1
    else:
        return con(n-1, m) + con(n-1, m-1)

n = 1
while n != -1:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    if n == -1:
        break
    elif n <= 0 or m <= 0:
        print("0보다 큰 수를 입력해주세요")
    elif n < m:
        print("n을 m보다 크거나 같게 입력해주세요")
    else:
        print (con(n,m)) 
