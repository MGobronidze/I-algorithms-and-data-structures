#ორი რიცხვის გადამრავლება იტერაციული გადაჭრა
def mult_iter(a,b):
    res = 0
    while b > 0:
        res += a
        b -= 1
    return res
print(mult_iter(30,11))

#ორი რიცხვის გადამრავლება იტერაციული გადაჭრა
def mult_rec(a,b):
    if b == 1:
        return a
    else:
        return a+ mult_rec(a, b-1)
    
print(mult_rec(15,7))

# ფაქტორიალი რეკურსიული მიდგომა
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))


# ფაქტორიალი იტერაციული მიდგომა
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i 
    return prod

print(fact_iter(6))

# ჰანოის კოშკები
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(4, 3, 2, 1)

# ფიბონაჩი
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(6))

# პალინდრომი
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

print(isPalindrome("abba"))

# solutions
# 1
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  

#2
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))

print(find_max([3, 1, 7, 9, 2]))  

#3
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))  

#4
def search_element(lst, target):
    if not lst:
        return False
    if lst[0] == target:
        return True
    return search_element(lst[1:], target)

print(search_element([1, 2, 3, 4, 5], 3)) 
print(search_element([1, 2, 3, 4, 5], 6)) 

#5
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    return lst[0] <= lst[1] and is_sorted(lst[1:])

print(is_sorted([1, 2, 3, 4, 5])) 
print(is_sorted([1, 3, 2, 4, 5])) 
