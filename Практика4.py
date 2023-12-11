#номер 1
'''def find_value(arr, k, sort_type):
    left, right = 0, len(arr) - 1
    found_index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            found_index = mid
            if sort_type == 1:
                right = mid - 1  # Для поиска первого вхождения в возрастающем порядке
            else:
                left = mid + 1   # Для поиска первого вхождения в убывающем порядке
        elif arr[mid] < k:
            if sort_type == 1:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if sort_type == 1:
                right = mid - 1
            else:
                left = mid + 1

    return found_index
arr=[1,5,7,8,4,3,2,1,2,3,4,9,6,7,9,0,6]
arr.sort()
print(arr)
k=6
sort_type=1
ans=find_value(arr, k, sort_type)
print(ans)'''
#номер 2
'''Программа сначала определяет перекрытие между всеми парами строк, 
затем объединяет строки с максимальным перекрытием. 
Процесс повторяется до тех пор, пока не останется одна строка. 
Длина этой строки выводится как результат.'''
'''def shortest_superstring(strings):
    while len(strings) > 1:
        max_overlap = float('-inf')
        best_pair = (0, 1)

        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                overlap = find_overlap(strings[i], strings[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_pair = (i, j)

        i, j = best_pair
        merged_string = merge_strings(strings[i], strings[j])
        strings.pop(j)
        strings[i] = merged_string

    return len(strings[0])

def find_overlap(str1, str2):
    max_overlap = 0
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1.endswith(str2[:i]):
            max_overlap = i
    return max_overlap

def merge_strings(str1, str2):
    overlap = find_overlap(str1, str2)
    return str1 + str2[overlap:]

# Ввод числа n
n = int(input("Введите число строк (0 < n <= 10): "))

# Ввод строк
strings = []
for i in range(n):
    string = input(f"Введите строку {i + 1}: ")
    strings.append(string)

# Вычисление и вывод длины самой короткой строки
result = shortest_superstring(strings)
print(f"Длина самой короткой строки: {result}")'''
#номер 3
'''def count_combinations(sequence, target_sum, index, current_sum):
    if current_sum == target_sum:
        return 1

    if index == len(sequence):
        return 0

    # Включаем текущий элемент в комбинацию
    include_current = count_combinations(sequence, target_sum, index + 1, current_sum + sequence[index])

    # Исключаем текущий элемент из комбинации
    exclude_current = count_combinations(sequence, target_sum, index + 1, current_sum)

    return include_current + exclude_current

def main():
    # Чтение числа n из стандартного ввода
    n = int(input())

    # Чтение последовательности из n чисел
    sequence = list(map(int, input().split()))

    # Вычисление суммы чисел в последовательности
    sequence_sum = sum(sequence)

    # Подсчет комбинаций с суммой, равной степени числа n
    result = count_combinations(sequence, sequence_sum, 0, 0)

    # Вывод результата
    print(result)

if __name__ == "__main__":
    main()'''
#номер 4
'''def bidirectional_bubblesort(arr):
    n = len(arr)
    for i in range(n // 2):
        # Flag to check if any swap is made in a pass
        swapped = False
        
        # Left to right pass
        for j in range(i, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Right to left pass
        for j in range(n - i - 2, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        
        # If no swaps were made in a pass, the array is sorted
        if not swapped:
            break

    return arr'''