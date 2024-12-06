#method1 converting into string and calculating sum
def SumDigit(number):
    sum_digits=0
    for char in number:
        sum_digits+=int(char)
    return sum_digits
number=input()
print(SumDigit(number))

#method 2 modulo(%)operator
def SumDigit(number):
    sum_digits=0
    while number!=0:
        sum_digits+=number%10
        number=number//10
    return sum_digits
number=int(input())
print(SumDigit(number))

#method 3 sum()
num=input()
number=[int(d) for i in num]
print(sum(number)

#method 4 using ASCII Values
num=input()
sum_digits=0
for i in num:
    sum_digits+=ord(i)-48# here we are using the ord() to get the ascii value of numbers the 48 is ascii code for 0
print(sum_digits)
