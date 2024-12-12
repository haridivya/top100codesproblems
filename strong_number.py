num=input()
strong_number=0
fact=1
for i in num:
    n=int(i)
    if i==1:
        strong_number+=1
    else:
        fact=1
        for x in range(2,n+1):
            fact*=x
        strong_number+=fact
if int(num)==strong_number:
    print(num," is a Strong Number")
else:
    print(num,"is Not a strong number")
            
