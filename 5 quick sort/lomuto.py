# Helper swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

# QuickSort function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Driver code to test the QuickSort
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("Sorted array:", arr)
