def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
print(Repeat(list1))

# l1 = [ 2, 3, 0, 5, 1, 1, 2 ]
# l2 =[ 3, 0, 5, 1]
# if (list(set(l2)-set(l1))) == []:
#     print('yes')
# else:
#     print('no')


# def fibonacci(num):
#     f_num = 0
#     s_num = 1
#     if num <=0:
#         print('incorrect input')
#     elif num ==1:
#         return s_num
#     else:
#         for i in range(2,num):
#             t_num = f_num + s_num
#             f_num = s_num
#             s_num = t_num
#         return s_num
#
#
# print(fibonacci(5))

# A Utility Function to find the common
# prefix between first and last strings
def commonPrefixUtil(str1, str2):
    # n1 = len(str1)
    # n2 = len(str2)
    #
    result = ""

    # j = 0
    # i = 0
    # while (i <= n1 - 1 and j <= n2 - 1):
    #     if (str1[i] != str2[j]):
    #         break
    #     result += (str1[i])
    #
    #     i += 1
    #     j += 1
    l1 = list(str1)
    l2 = list(str2)
    print(str1,str2)
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            result = result+l1[i]
        else:
            break

    return result


def commonPrefix(arr, n):
    arr.sort(reverse=False)
    print(arr)
    print(commonPrefixUtil(arr[0], arr[n - 1]))


if __name__ == '__main__':
    arr = ["geeksforgeeks", "geeks",
           "geek", "geezer"]
    n = len(arr)

    commonPrefix(arr, n)

