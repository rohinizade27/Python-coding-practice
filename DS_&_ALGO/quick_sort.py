def get_pivot_place(high,low,arr):
    pivot = arr[0]
    left = low+1
    right = high

    while left<=right and arr[left]<=pivot:
        left = left+1
    while left<=right and arr[right]>=pivot:
        right = right-1

    while True:
        if left>right:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right


def quick_sort(high,low,arr):
    if low<high:
        p = get_pivot_place(high,low,arr)
        quick_sort(high,p+1,arr)
        quick_sort(p-1,low,arr)


num = int(input("size of array:"))
arr = [int(input()) for i in range(num)]  # list comprehension
n = len(arr)
quick_sort(n-1,0,arr)
print(arr)