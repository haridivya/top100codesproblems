#method 1 using if-else
number=int(input())
def prime_number(number):
    n=0
    if number==2:
        return "prime"
    else:
        for i in range(2,number):
            if number%i==0:
                n=1
    if n==0:
        return "Prime number"
    else:
        return "Not a prime number"
print(prime_number(number))

#method 2 recursion
num = int(input())
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
  print("Prime")
else:
  print("Not Prime")

#method 3 using n/2
number=int(input())
def prime_number(number):
    n=0
    if number==2:
        return "prime"
    else:
        for i in range(2,int(number/2)+1):
            if number%i==0:
                n=1
    if n==0:
        return "Prime number"
    else:
        return "Not a prime number"
print(prime_number(number))


