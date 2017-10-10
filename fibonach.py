import time

#재귀함수를 통한 피보나치수열
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

#반복문을 통한 피보나치수열
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

#두개 시간비교
while True:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(n)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (n, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(n)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (n, fibonumber, ts))