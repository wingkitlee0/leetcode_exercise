import math

def merge(L, R):
    """merge two sorted arrays"""
    print("Merging ", L, " ", R)
    if L[-1] < R[0]:
        for r in R:
            L.append(r)
        return L
    if R[-1] < L[0]:
        for l in L:
            R.append(l)
        return R

    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    if i==len(L):
        for r in R[j:]:
            result.append(r)
    if j==len(R):
        for l in L[i:]:
            result.append(l)
    return result

def mergeSort(arr):
    """merge sort"""
    print("Sorting ", arr)

    N = len(arr)
    if N==1:
        return arr
    elif N==2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr
    else:
        L = mergeSort(arr[:math.ceil(N/2)])
        R = mergeSort(arr[math.ceil(N/2):])
        return merge(L, R)


if __name__ == '__main__':
    print("Sort [3,1] = ",  mergeSort([3,1]) )
    print("Sort [3,1,2] = ",  mergeSort([3,1,2]) )
    print("Sort [3,1,2,4] = ",  mergeSort([3,1,2,4]) )
    print("Sort [38, 27, 43, 3, 9, 82, 10] = ",  mergeSort([38, 27, 43, 3, 9, 82, 10]) )