
def binarysearch(arr,start,end,t):

    if end >= start:
        mid = start + (end-start) // 2   # best practice instead of (start+end)//2

        if t == arr[mid]:
            return mid
        elif t < arr[mid]:
            return binarysearch(arr,start,mid-1,t)
        elif t > arr[mid]:
            return binarysearch(arr,mid+1,end,t)

    return -1



print('hello')
arr = [3,9]
arrlen = len(arr)
start = 0
end = arrlen-1
t = 9
print(binarysearch(arr,start,end,t))