#задание номер 3(второй способ)
"""row = int(input())
column = int(input())
arr = []
for i in range(row):
    arr.append(list(map(int, input().split())))
saddle_elem = None
for i in range(row):
    for j in range(column):
        elem = arr[i][j]
        if elem == max(arr[i]) and elem == min([x[j] for x in arr]):
            saddle_elem = elem
print(saddle_elem)"""

#задание номер 2
"""n=int(input())
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)
k=int(input())
s=a[0]+a[1]
for i in range(0,n-1):
    if a[i]+a[i+1]>s:
        s=a[i]+a[i+1]"""
#задание 3
"""def resheto_eratosfena(n):
    a=[i for i in range(n+1)]
    a[1]=0
    i=2
    while i<=n/2:
        if a[i]!=0:
            j=i+i
            while j<=n:
                a[j]=0
                j=j+i
        i=i+1
    return a
#print(resheto_eratosfena(int(input())))
n=int(input())
b=[]
a=resheto_eratosfena(n)
for e in a:
    if e!=0:
        if n%e==0:
            b.append(e)
print(max(b))"""
#задание 1
"""import sys
 
 
# Функция нахождения максимальной суммы непрерывного подмассива
# в заданном целочисленном массиве (также обрабатывает отрицательные числа)
def kadaneNeg(arr):
    # хранит подсписок максимальной суммы, найденный на данный момент.
    max_so_far = -sys.maxsize
 
    # хранит максимальную сумму подсписков, заканчивающихся на текущей позиции
    max_ending_here = 0
 
    # пройти по заданному списку
    for i in range(len(arr)):
        # обновляет максимальную сумму подсписка, «заканчивающегося» на индексе «i» (путем добавления
        # текущий элемент до максимальной суммы, заканчивающейся на предыдущем индексе 'i-1')
        max_ending_here = max_ending_here + arr[i]
 
        # Максимальная сумма # должна быть больше, чем текущий элемент
        max_ending_here = max(max_ending_here, arr[i])
 
        # обновляет результат, если сумма текущего подсписка оказывается больше
        max_so_far = max(max_so_far, max_ending_here)
 
    return max_so_far
 
 
if __name__ == '__main__':
 
    arr = [-8, -3, -6, -2, -5, -4]
    print('The sum of contiguous sublist with the largest sum is', kadaneNeg(arr))"""
    
    
