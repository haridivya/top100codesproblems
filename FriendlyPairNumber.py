#Friendly Pair
#Using with list comprehension and sum Method
num1=int(input("Enter a Number:))
num2=int(input("Enter a Number:))
num1_divisor=[i for i in range(1,num1+1) if num1%i==0]
num2_divisor=[i for i in range(1,num2+1) if num2%i==0]
n1=sum(num1_divisor)//num1
n2=sum(num2_divisor)//num2
print('Friendly pair') if n1==n2 else print("Not friendly pair")
