# Сортировка "пузырьком" (императивный стиль)
def bubble_sort_imperative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортировка "пузырьком" (декларативный стиль)
def bubble_sort_declarative(numbers):
    numbers.sort(reverse=False)
    return numbers


print(f"Imperative style -> {bubble_sort_imperative([41, 6, 2, 7, -3, 2, 8, 56])}")
print(f"Declarative style -> {bubble_sort_declarative([41, 6, 2, 7, -3, 2, 8, 56])}")