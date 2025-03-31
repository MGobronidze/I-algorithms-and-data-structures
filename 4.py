# insertion sort
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

# Driver code to test the function
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    
    insertionSort(arr)
    
    print("Sorted array:", arr)

# merge sort
# def merge_sort(arr):
#     if len(arr) > 1:
#         # მასივის გაყოფა შუაში
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         # რეკურსიული გამოძახება
#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         # ელემენტების შერწყმა და დალაგება
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         # დარჩენილი ელემენტების გადატანა
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# # დრაივერ კოდი - ტესტირება
# if __name__ == "__main__":
#     test_arr = [38, 27, 43, 3, 9, 82, 10]
#     print("დალაგებამდე:", test_arr)
#     merge_sort(test_arr)
#     print("დალაგების შემდეგ:", test_arr)
