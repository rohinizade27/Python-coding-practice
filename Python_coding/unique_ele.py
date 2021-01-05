def find_unique(li):
    unq_li = []
    for ele in li:
        if ele  not in unq_li:
            unq_li.append(ele)
    return unq_li


li =[10, 20, 10, 30, 40, 40]
print(find_unique(li))