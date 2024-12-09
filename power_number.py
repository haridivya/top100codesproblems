#method 1:pow()
n=int(input())
power=int(input())
def power_number(n,power):
    return pow(n,power)
print(power_number(n,power))

#method 2:using operator
n=int(input())
power=int(input())
def power_number(n,power):
    return n**power
print(power_number(n,power))

#method 3 iteration method
n=int(input())
power=int(input())
def power_number(n,power):
    result=1
    for i in range(power):
        result*=n
    return result
print(power_number(n,power))
