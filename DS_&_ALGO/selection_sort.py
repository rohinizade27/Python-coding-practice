# using min and index method
# def selection_sort(arr):
#     for i in range(0,len(arr)-1):
#         min_value = min(arr[i:])
#         min_index = arr.index(min_value,i)
#         if arr[i] != arr[min_index]:
#             arr[i],arr[min_index]=arr[min_index],arr[i]
#         # print(arr)
#     return arr

def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        if arr[i] != arr[min_index]:
            arr[i],arr[min_index]=arr[min_index],arr[i]
        # print(arr)
    return arr


my_list =[25,21,5,4,33,4]
print(my_list)
print(selection_sort(my_list))