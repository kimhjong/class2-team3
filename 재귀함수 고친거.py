def con(n,m):  
    if m == 1:
        return n
    elif m < 0:
        return 0
    elif n == 0 and m == 0:
        return 1
    elif n == m:
        return 1
    else:
        return con(n-1, m) + con(n-1, m-1)

n = 1
try:
    while n != -1:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
        if n == -1:
            break
        elif n < 0 or m < 0:
            print("0이상 인 수를 입력해주세요")
        elif n == 0 and m > 0:
            print(0)
        elif n == 0 and m == 0:
            print(1)
        elif n > 0 and m == 0:
            print("다시 입력해 주세요")
        elif n < m:
            print("n을 m보다 크거나 같게 입력해주세요")
        else:
            print (con(n,m))
except ValueError:
    print("잘못 입력하셨습니다. 종료합니다")
