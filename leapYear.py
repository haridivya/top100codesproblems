#Method 1 using if-else
def leap_year(year):
    if year%400==0 or year%4==0 and year%100!=0:
            return "leap year"
    else:
            return "not a leap year"
year=int(input())
print(f'{year} {leap_year(year)}')

#Method 2 using ternary operator
def leap_year(year):
    return (year%400==0 or year%4==0) and year%100!=0
year=int(input())
result=leap_year(year)
print(f"{year} is a Leap Year") if result==True else print(f"{year} is not a leap year")

#method 3
import calendar
year=int(input())
if calendar.isleap(year):
	print("Leap year")
else:
	print("not a leap year")
