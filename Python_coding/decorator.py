def wrapper(f):
    def fun(l):
        new_list =[]
        for ele in l:
            if ele[0] in['0',0]:
                new_list.append('+91 '+ele[1:6]+' '+ele[6:])
            elif len(ele)== 10 and ele[0:2] in ['91',91]:
                new_list.append('+91 '+ele[0:5]+' '+ele[5:])
            elif len(ele)== 10 and ele[0:2] not in ['91',91]:
                new_list.append('+91 '+ele[0:5]+' '+ele[5:])
            elif len(ele)> 10 and ele[0:2] in ['91',91]:
                new_list.append('+91 '+ele[2:7]+' '+ele[7:])
            elif ele[0:3] in ['+91',+91]:
                new_list.append('+91 '+ele[3:8]+' '+ele[8:])
        return f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)