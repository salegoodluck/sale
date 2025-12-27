def quick_sort(arr):
    """快速排序算法"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print("原始数组:", numbers)
    sorted_numbers = quick_sort(numbers)
    print("排序后数组:", sorted_numbers)
