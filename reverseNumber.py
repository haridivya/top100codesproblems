#method 1 string slicing
number=input()
print(int(number[::-1]))

#method 2 using reverse function
number=input()
digit=[i for i in number]
digit.reverse()
print("".join(digit))

#method 3
num = int(input())
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)
