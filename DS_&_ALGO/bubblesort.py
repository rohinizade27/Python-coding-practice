def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(arr)
    return arr

my_list =[25,21,5,4,33]
print(bubble_sort(my_list))