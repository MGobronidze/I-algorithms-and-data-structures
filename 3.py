import math
# იტერაციული ორობითი ძებნა
# def binarySearch(arr, low, high, x):
#     while low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# if __name__ == '__main__':
#     arr = [2, 3, 4, 10, 40]
#     x = 10
#     result = binarySearch(arr, 0, len(arr) - 1, x)
#     if result != -1:
#         print("Element is present at index", result)
#     else:
#         print("Element is not present in array")


# # რეკურსიული ორობითი ძებნა
# def binarySearch(arr, low, high, x):
#     if high >= low:
#         mid = low + (high - low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, low, mid - 1, x)
#         else:
#             return binarySearch(arr, mid + 1, high, x)
#     else:
#         return -1

# if __name__ == '__main__':
#     arr = [2, 3, 4, 10, 40]
#     x = 10
#     result = binarySearch(arr, 0, len(arr) - 1, x)
#     if result != -1:
#         print("Element is present at index", result)
#     else:
#         print("Element is not present in array")

# # ყველა ქვესიმრავლეთა სიმრავლე
def printPowerSet(set, set_size):
    pow_set_size = (int)(math.pow(2, set_size))

    for counter in range(0, pow_set_size):
        for j in range(0, set_size):
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
        print("")

set = ['a', 'b', 'c', 'd']
printPowerSet(set, 4)


# # ყველა ქვესიმრავლეთა სიმრავლის პოვნა, რეკურსიული ალგორითმი
# def genSubsets(L):
#     res = []
#     if len(L) == 0:
#         return [[]]  # ცარიელი სიის სია
#     smaller = genSubsets(L[:-1])  # ყველა ქვემონაცემი ბოლო ელემენტის გარეშე
#     extra = L[-1:]  # მხოლოდ ბოლო ელემენტი
#     new = []
#     for small in smaller:
#         new.append(small + extra)  # ყველა მცირე შედეგისთვის, დაამატე ბოლო ელემენტი
#     return smaller + new  # გააერთიანე შედეგები

# print(genSubsets(['a', 'b']))
