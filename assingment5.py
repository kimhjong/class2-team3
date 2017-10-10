import time

def iterfibo(n):
    past = 0 
    current = 1
    storage = 1
    if (n == 0):
         return 0
    elif (n == 1):
        return 1
    else:
        for i in range(2, n+1):
            storage = current
            current = past + current
            past = storage 
    return current

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

try:
    while True:
        n = int(input("0이상의 숫자를 입력하세요: "))
        if n == -1:
            break
        if n >= 0:
            ts = time.time()
            fibonumber = iterfibo(n)
            ts = time.time() - ts
            print("IterFibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
            ts = time.time()
            fibonumber = fibo(n)
            ts = time.time() - ts
            print("Fibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
        if n < 0:
            print("잘못 입력하셨습니다. 0이상의 숫자를 입력해 주세요")
except ValueError:
    print("잘못 입력하셨습니다. 종료합니다.") 
except RecursionError:
    print("숫자가 너무 커서 재귀문이 감당하지 못합니다. 종료합니다.")      
