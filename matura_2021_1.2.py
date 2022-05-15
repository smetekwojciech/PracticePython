
n=int(7654)
d=0
i=1
# n = x1*1000 + x2*100 + x3*10 + x4*1



while n!=0:
    r=n%10
    if(i!=1000):
        wynik=(9-r)*i
    elif(i==1000):
        wynik=(8-r)*i
    d+=wynik
    n=n//10
    i*=10
print(d)    