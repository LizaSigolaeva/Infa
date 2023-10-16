"""praktica dz 2"""
#номер 5
"""def factorial (x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
x=int(input())
y=factorial(x)
print(factorial(x))
y=str(y)
print(y.count('0'))"""
#номер 6
"""n=int(input())
k=int(input())
s=[i for i in range(1,n+1)]
while len(s)>1:
    for q in range(0,k-1):
        s.append(s[q])
    del s[:k]
print(s)"""
#не помню какой номер,скорее всего первый
"""n=int(input())
x0=int(input())
a=[]
for i in range(n+1):
    a.append(int(input()))
f=0
f2=0
k=n
for i in range(n+1):
    print(a[k],x0**k,k)
    f=f+(a[k]*(x0**k))
    k=k-1
print(f)
k=n
for i in range(n+1):
    if k!=0:
    #print(a[k]*k,"*x0**",k-1)
        f2=f2+a[k]*k*(x0**(k-1))
    k=k-1
print(f2)
"""
#номер 2

"""a=int(input())
b=int(input())
m=int(input())
print((a*b)%m)
n=0
c=b
while c>0:
    n+=1
    c//=2
c=b
b2=[]
for i in range (n-1,-1,-1):
    b2.append(c%2)
    c//=2
#for i in range (0,n):
    #print (b2[i])
    
P=a*b2[n-1]*2+a*b2[n-2]
for i in range (n-2,0,-1):
    f=P
    P=a*b2[i-1]+2*f
#print(P)
print (P%m)
x=int(input())
y=int(input())
print((x+y)%m)
print(((x%m)+(y%m))%m)"""
    
    
