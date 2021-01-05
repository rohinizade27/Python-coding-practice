def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if key==arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid-1
        else:
            low = mid +1
    return -1


arr = [22,66,77,88,99]
key = 44
print(binary_search(arr,key))


def binary_serach(arr,l,r,key):
    if l <=r:
        mid = l +r//2
        if key==arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_serach(arr,l,mid-1,key)
        else:
            return binary_serach(arr,mid+1,r,key)
    else:
        return -1

arr = [22,66,77,88,99]
key = 77
print(binary_serach(arr,0,len(arr)-1,key))