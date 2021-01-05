# def mergeSort(arr):
#     if len(arr) > 1:  # base condition to stop dividing arr
#         # divide arr till it contain more than one ele
#         mid = len(arr) // 2  # find mid point of arr
#         left_arr = arr[:mid]  # divide arr in to halves
#         right_arr = arr[mid:]
#
#         mergeSort(left_arr)  # first half
#         mergeSort(right_arr)  # sencod half
#
#         i, j, k = 0, 0, 0  # i will point to left_arr
#         # j will point to right_arr
#         # k will point to arr(here we will merge element)
#         while (i < len(left_arr) and j < len(right_arr)):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]  # if left_arr ele is lesser than right then append it to
#                 # arr at kth position
#                 i = i + 1
#                 k = k + 1
#             else:
#                 arr[k] = right_arr[j]  # else  append right_arr  to arr at kth position
#                 j = j + 1
#                 k = k + 1
#
#         # Checking if any element was left
#         while (i < len(left_arr)):
#             arr[k] = left_arr[i]
#             i = i + 1
#             k = k + 1
#         while (j < len(right_arr)):
#             arr[k] = right_arr[j]
#             j = j + 1
#             k = k + 1


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lifgt_arr =arr[:mid]
        right_arr = arr[mid:]

        mergeSort(lifgt_arr)
        mergeSort(right_arr)

        i=0
        j=0
        k=0
        while i < len(lifgt_arr) and j<len(right_arr):
            if lifgt_arr[i]<right_arr[j]:
                arr[k]=lifgt_arr[i]
                i = i+1
                k = k+1
            else:
                arr[k]=right_arr[j]
                j = j+1
                k = k+1
        while i < len(lifgt_arr):
            arr[k]=lifgt_arr[i]
            i = i+1
            k = k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1





num = int(input("size of array:"))
arr = [int(input()) for i in range(num)]  # list comprehension
mergeSort(arr)
print(arr)