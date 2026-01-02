def quicksort(arr):
    """
    快速排序算法
    :param arr: 待排序列表
    :return: 排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def bubble_sort(arr):
    """
    冒泡排序算法
    :param arr: 待排序列表
    :return: 排序后的新列表
    """
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

if __name__ == "__main__":
    # 示例用法
    test_list = [3, 6, 8, 10, 1, 2, 1]
    print("原始列表:", test_list)
    print("快速排序结果:", quicksort(test_list))
    print("冒泡排序结果:", bubble_sort(test_list))
