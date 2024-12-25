number=input("Enter a Number:")
replace_num=''
for i in number:
    if int(i)==0:
        replace_num+='1'
    else:
        replace_num+=i
print(int(replace_num))
