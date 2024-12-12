n=int(input("Enter a number:"))
perfect_num=0
for i in range(1,n):
    if n%i==0:
        perfect_num+=i
if n==perfect_num:
    print('perfect Number')
else:
    print("Not a perfect number")
