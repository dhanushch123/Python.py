class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self,self2):
        new_num = (self.num)*(self2.den) + (self2.num)*(self.den)
        new_den=(self.den)*(self2.den)
        return self.simplification(new_num, new_den)
    def __sub__(self,self2):
        new_num = (self.num) * (self2.den) - (self2.num) * (self.den)
        new_den = (self.den) * (self2.den)
        return self.simplification(new_num, new_den)
    def __mul__(self,self2):
        new_num = (self.num)*(self2.num)
        new_den = (self.den) * (self2.den)
        return self.simplification(new_num, new_den)
    def __truediv__(self,self2):
        new_num = (self.num)*(self2.den)
        new_den = (self.den)*(self2.num)
        return self.simplification(new_num,new_den)
    def simplification(self,new_num,new_den):
        gcdn=self.gcd(new_num,new_den)
        new_num = new_num//gcdn
        new_den = new_den//gcdn
        if new_num==0 and new_den>0:
            return f"{new_num}"
        return f"{new_num}/{new_den}"
    def gcd(self,new_num,new_den):
        gc_div=1
        for i in range(1,min(new_num,new_den)+1):
            if new_num%i==0 and new_den%i==0:
                gc_div=i
        return gc_div


x=Fraction(16,32)
print(x)
y=Fraction(32,64)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
