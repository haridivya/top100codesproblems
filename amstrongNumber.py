#method 1
num=input()
n=len(num)
amstrong=0
for i in num:
    amstrong+=int(i)**n
if int(num)==amstrong:
    print("Amstrong Number")
else:
    print("Not A amstrong number")
    
