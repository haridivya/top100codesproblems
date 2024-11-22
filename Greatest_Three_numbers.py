'''
To find out Greatest Number between Given three Numbers
'''
#Method 1:
#If-else
num1=int(input())
num2=int(input())
num3=int(input())
print(max(num1,num2,num3))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)

#Method 2:
#by using built-in method max()
num1=int(input())
num2=int(input())
num3=int(input())
print(max(num1,num2,num3))
#method 3:
#ternary operator
num1=int(input())
num2=int(input())
num3=int(input())
max_value=num1 if num1>num2  else num2
max_value=num2 if num3>max_value else num3
print(max_value)

