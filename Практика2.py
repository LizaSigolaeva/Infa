#Номер 1
'''Программа будет использовать два указателя - левый и правый. 
Они будут указывать на начало и конец текущего окна из k элементов. 
Мы будем сдвигать правый указатель, учитывая новый элемент, и при необходимости сдвигать левый указатель, 
чтобы поддерживать окно длины k. 
Таким образом, сумма элементов в окне будет обновляться за константное время.'''
'''def maxk(arr, n, k):
    if k > n or k <= 0:
        return "Invalid value of k"

    max_sum = sum(arr[:k])
    current_sum = max_sum

    left, right = 0, k

    while right < n:
        current_sum += arr[right] - arr[left]
        if current_sum > max_sum:
            max_sum = current_sum
        left += 1
        right += 1

    return max_sum

# Считываем размер массива, его элементы и число k
n = int(input("Введите размер массива: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]
k = int(input("Введите число k: "))

# Выводим максимальную сумму k последовательных элементов
result = maxk(arr, n, k)
print(f"Максимальная сумма {k} последовательных элементов: {result}")'''
#номер 2
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
#номер 3
def find_saddle_point(matrix):
    strr = len(matrix)
    stolb = len(matrix[0])

    for i in range(strr):
        saddle_strr = 0
        for j in range(1, stolb):
            if matrix[i][j] > matrix[i][saddle_strr]:
                saddle_stolb = j

        saddle_stolb = 0
        for k in range(1, strr):
            if matrix[k][saddle_stolb] < matrix[saddle_strr][saddle_stolb]:
                saddle_strr = k

        # Проверка, является ли элемент седловым
        if saddle_strr == i:
            return saddle_strr, saddle_stolb

    # Седловая точка не найдена
    return None

# Ввод количества строк и столбцов
strr, stolb = map(int, input("Введите количество строк и столбцов (не более 10): ").split())

# Ввод элементов массива
matrix = []
print("Введите элементы массива:")
for i in range(strr):
    strr = list(map(int, input().split()))
    matrix.append(strr)

# Поиск и вывод седловой точки
result = find_saddle_point(matrix)
if result is not None:
    print(f"Седловая точка: {result}")
else:
    print("none")
