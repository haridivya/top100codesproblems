'''
Given an integer input as the number, the objective is to Find all the Prime Factors of a the given integer input number. 
Therefore, we’ll write a program to Find the Prime Factors of a Number in Python Language.
'''
n=int(input("Enter a number:"))
factor=[]
prime_factors=[]
for i in range(2,n):
    if n%i==0:
        factor.append(i)
count=0
for i in factor:
    if i==2:
        prime_factors.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                count=1
                break
        if count==0:
            prime_factors.append(i)
print(prime_factors)
        
