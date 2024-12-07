#method 1 
num=int(input())
temp=num
reverse=0
while num!=0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num//=10
if reverse==temp:
    print("palindrome")
else:
    print("Not palindrome")
#method2 string Slicing
num=input()
reverse=num[::-1]
if num==reverse:
    print("Palindrome")
else:
    print("Not a paildrome")
#method 3 builtin function
num=input()
reve=''.join(reversed(num))
if num==reve:
    print("palindrome")
else:
    print("Not a paildrome")
