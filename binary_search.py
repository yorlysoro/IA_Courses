def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Devuelve el índice donde se encontró el objetivo
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Devuelve -1 si el objetivo no está en la lista