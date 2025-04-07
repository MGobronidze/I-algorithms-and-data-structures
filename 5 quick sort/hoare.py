# Hoare partition scheme
def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Find leftmost element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Find rightmost element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If two pointers met
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# QuickSort using Hoare partition
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

# Utility function to print array
def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [8, 4, 7, 9, 3, 10, 5]
    print("Original array:")
    printArray(arr)

    quickSort(arr, 0, len(arr) - 1)

    print("Sorted array:")
    printArray(arr)
