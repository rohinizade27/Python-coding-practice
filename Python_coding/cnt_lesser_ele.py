def count_lesser_ele(arr, high , low):
    arr.sort()
    mid = (low+high)//2
    while low < high:
        if arr[mid] < key and arr:
            return mid
        elif arr[mid +1] < arr[mid]:
            return mid+1

        if (arr[high] > arr[mid]):
            return rotate_binary(arr, mid - 1,low);

        return rotate_binary(arr, high,mid + 1)

arr = [30,40,50,10,20]
arr = [10,20,25,30,40,50]
key = 35
high = len(arr) - 1
low = 0
print(count_lesser_ele(arr,high,low,key))