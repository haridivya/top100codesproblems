'''
#There are 3 way to find out the Greatest of Two Number
#Method 1:
#by using the if-else condition 
'''
num1=int(input())#10
num2=int(input())#12
if num1>num2:#10>12 False
    print(num1)
else:
    print(num2)
#Method 2:
#By using the Ternary Operator
num1=int(input())
num2=int(input())
print(num1) if num1>num2 else print(num2)

#Method 3:
#By using the builtin-method
num1=int(input())
num2=int(input())
print(max(num1,num2))

