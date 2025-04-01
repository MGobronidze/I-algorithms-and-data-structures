# Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        # Splitting the array in half
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merging and sorting elements
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copying remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Testing Merge Sort
test_arr = [38, 27, 43, 3, 9, 82, 10]
print("Before Merge Sort:", test_arr)
merge_sort(test_arr)
print("After Merge Sort:", test_arr)
print("\n" + "-"*40 + "\n")

# Testing Insertion Sort
arr = [12, 11, 13, 5, 6]
print("Before Insertion Sort:", arr)
insertionSort(arr)
print("After Insertion Sort:", arr)
