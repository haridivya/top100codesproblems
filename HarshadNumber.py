#To find out the given number is a harshad number or not
#A Harshad number is an integer that is divisible by the sum of its digits in a given number base 
# ex:21 the sum of 21 is 3 and 21/3=0
class Harshad_Number:
    def checkNumber(self, num):
        temp=num
        sum_num = 0
        while num>0:
            sum_num += num % 10
            num //= 10
        return "Harshad Number" if temp%sum_num==0 else "Not a harshad number"
obj=Harshad_Number()
num=int(input("Enter a number:"))
print(obj.checkNumber(num))
