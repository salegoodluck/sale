def bubble_sort(arr):
    """冒泡排序算法"""
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", numbers)
    sorted_numbers = bubble_sort(numbers.copy())
    print("排序后数组:", sorted_numbers)
