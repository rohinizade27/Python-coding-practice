
def rotate_arr(arr):
   min_value = arr[0]
   for i in range(len(arr)):
       if arr[i] < min_value:
           min_value = arr[i]
           index_min_val = arr.index(min_value)
   print(index_min_val)

arr = [40,50,10,20,30]
rotate_arr(arr)


def rotate_binary(arr, high , low):
    mid = (low+high)//2
    while low < high:
        if arr[mid] < arr[mid-1]:
            return mid
        elif arr[mid +1] < arr[mid]:
            return mid+1

        if (arr[high] > arr[mid]):
            return rotate_binary(arr, mid - 1,low);

        return rotate_binary(arr, high,mid + 1)

arr = [30,40,50,10,20]
high = len(arr) - 1
low = 0
print(rotate_binary(arr,high,low))

