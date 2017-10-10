import time

#재귀함수를 통한 피보나치수열
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

#반복문을 통한 피보나치수열
def iterfibo(n):
    r1 = 1
    r2 = 1
    r3 = 0
    if n == 1 or n == 2:
        return 1

    else:
        for i in range(0,n-2):
            r3 = r2 + r1
            r1 = r2
            r2 = r3
        return r3


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