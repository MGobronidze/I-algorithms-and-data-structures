import math
#1 ფიბონაჩი
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
#2 ფიბონაჩი - იტერაციული ალგორითმი
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        fib_i = 0  
        fib_ii = 1 
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii             
            fib_ii = tmp + fib_ii     
        return fib_ii
    
#3 ორი რიცხვის გადამრავლება იტერაციული გადაჭრა
def mult_iter(a,b):
    res = 0
    while b > 0:
        res += a
        b -= 1
    return res
print(mult_iter(30,11))

#4 ორი რიცხვის გადამრავლება რეკურსიული გადაჭრა
def mult_rec(a,b):
    if b == 1:
        return a
    else:
        return a+ mult_rec(a, b-1)
    
#5 ფაქტორიალი რეკურსიული მიდგომა
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

#6 პალინდრომი
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#7  თანაკვეთის პოვნა
def intersect(L1, L2):
    tmp = []
    for el in L1:
        for e2 in L2:
            if el == e2:
                tmp.append(el)

    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)

    return res

#8  ჰანოის კოშკები
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

#9  სიმრავლის ყველა ქვესიმრავლის პოვნის ალგორითმი
def printPowerSet(set, set_size):
    pow_set_size = (int)(math.pow(2, set_size))

    for counter in range(0, pow_set_size):
        for j in range(0, set_size):
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
        print("")

#10 ყველა ქვესიმრავლეთა სიმრავლის პოვნა, რეკურსიული ალგორითმი
def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]  # ცარიელი სიის სია
    smaller = genSubsets(L[:-1])  # ყველა ქვემონაცემი ბოლო ელემენტის გარეშე
    extra = L[-1:]  # მხოლოდ ბოლო ელემენტი
    new = []
    for small in smaller:
        new.append(small + extra)  # ყველა მცირე შედეგისთვის, დაამატე ბოლო ელემენტი
    return smaller + new  # გააერთიანე შედეგები

#11 იტერაციული ორობითი ძებნა
def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#12  Insertion Sort
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

#13  Merge Sort
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

#14  სწრაფი დალაგება
# Helper swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function
def partition_lomuto(arr, low, high):
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
        pi = partition_lomuto(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

#15 Hoare partition scheme
def partition_hoare(arr, low, high):
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
        pi = partition_hoare(arr, low, high)

        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)