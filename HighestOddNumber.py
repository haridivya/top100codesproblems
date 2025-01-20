#To Ifnd Out Highest Odd Number
class OddNumber:
    def Highest_odd_number(self,number):
        self.num=number
        while self.num!=0:
            last_num=self.num%10
            if last_num%2==0:
                self.num//=10
            else:
                print(self.num,"highest odd number")
                break
nums=OddNumber()
number=int(input("Enter a Number:"))
nums.Highest_odd_number(number)
