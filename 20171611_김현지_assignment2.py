n = int(input("Enter a number: "))
 +
 +while n!= -1:
 +       if n>0:
 +          fact=1
 +          for i in range(1,n+1):
 +              fact=fact*i
 +          print(n,"!=",fact)
 +       elif n==0:
 +          print("0! = 1")
 +       elif n<-1:
 +          print("no answer")
 +
 +       n = int(input("Enter a number: "))
 Lock conversation
