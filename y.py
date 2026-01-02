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

if __name__ == "__main__":
    # 示例用法
    test_list = [3, 6, 8, 10, 1, 2, 1]
    print("原始列表:", test_list)
    print("排序结果:", quicksort(test_list))
