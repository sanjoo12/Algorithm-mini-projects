def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sorted_list = [11, 22, 25, 34, 64, 90]
    target = 34
    result = binary_search(sorted_list, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")
