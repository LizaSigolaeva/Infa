#Задание 4
'''def Peresechenie(A, B):
    # Создаем множество для хранения пересечения
    P = set()

    # Перебираем элементы первого множества
    for element in A:
        # Проверяем, есть ли элемент во втором множестве
        if element in B:
            # Если есть, добавляем его в множество пересечения
            P.add(element)

    return P
# Пример использования функции
A= {1,3,6,8,33,4,6,2,0,98}
B = {3,7,9,0,2,33}

P = Peresechenie(A, B)
print("Пересечение множеств:", P)'''
#Проверены 3,2,номер 4 изменить  способы задания множеств(вместо массивов списки,сделать поиск пересечения отдельной функцией)
#Задание 1
'''def f(coefficients, x):
    znach_polynoma = sum(coef * (x ** exp) for exp, coef in enumerate(coefficients))
    znach_proizvodnoy = sum(exp * coef * (x ** (exp - 1)) for exp, coef in enumerate(coefficients) if exp > 0)
    return znach_polynoma, znach_proizvodnoy

coefficients = [2, -1, 3]  # Пример: 2*x^2 - x + 3
t = 1.5

znach_polynoma, znach_proizvodnoy= f(coefficients, t)

print(f"Значение полинома в точке {t}: {znach_polynoma}")
print(f"Значение производной в точке {t}: {znach_proizvodnoy}")'''
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
#номер 3
'''x=int(input())
a=[]
while x>0:
 fm=0
 f0,f1=1,1
 index=0
 while fm<x:
  f0,f1=f1,f1+f0
  fm=f1
  index+=1
 a.append(index)
 x-=f0
f=['0']*max(a)
for i in a:
 f[i-1]='1'
f=''.join(f[::-1])
print(f)'''
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
