#abundant Number
class AbundantNumber:
    def number(self,num):
        sum_divisors=0
        for n in range(1,num):
            if num%n==0:
                sum_divisors+=n
        return "Abundant Number" if sum_divisors>num else "Not a Abundant Number"
abun=AbundantNumber()
num=int(input("Enter a Number:"))
print(abun.number(num))

