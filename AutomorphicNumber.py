#Check wheather the given number is automorphic or not
class Automorphic:
    def Number(self,n):
        power=n**2
        mod=10**len(str(n))
        return "Automorphic Number" if power%mod==n else "Not a Automorphic"
n=int(input())
auto=Automorphic()
print(auto.Number(n))

