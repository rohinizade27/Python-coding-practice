
# def insersion_sort(my_list):
#     for i in range(1,len(my_list)):
#         current_ele = my_list[i]
#         pos = i
#         while current_ele < my_list[pos-1] and pos > 0:
#             my_list[pos] = my_list[pos-1]
#             pos = pos -1
#         my_list[pos] = current_ele
#     return my_list

def insersion_sort(arr):
    for i in range(1,len(arr)):
        current_ele = arr[i]
        pos = i
        while arr[pos-1]>current_ele and pos>0:
            arr[pos] = arr[pos-1]
            pos = pos -1
        arr[pos] = current_ele
    return arr

my_list =[25,21,5,4,33]
print(my_list)
print(insersion_sort(my_list))