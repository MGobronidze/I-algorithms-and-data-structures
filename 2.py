
l1 = [3,5,6,7,3,2,2334,5667]
l2 = [3,2,4,5,67,8,9,35,5]
def isSubset(L1, L2):
    for el in L1:
        matched = False
        for e2 in L2:
            if el == e2:
                matched = True
                break
        if not matched:
            return False
    return True
print(isSubset(l1,l2))

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
print(intersect(l1,l2))

def find_min_max(A):
    min_elem = A[0]
    max_elem = A[0]

    for elem in A:
        if elem < min_elem:
            min_elem = elem
        if elem > max_elem:
            max_elem = elem

    return min_elem, max_elem
print(find_min_max(l1))