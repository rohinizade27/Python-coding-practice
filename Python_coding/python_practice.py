def sort_list(li):
    li.sort()
    print(li)
    new_li =[]
    size = len(li)-1
    while li:
        try:
            new_li.append(li[size])
            li.pop()
            new_li.append(li[0])
            li.pop(0)
            size = size - 2
        except:
            return new_li
    return new_li

li = [80,66,99,35,55,22,60]
print(sort_list(li))
###########################################################
class custom_dict:
    def __init__(self):
        self.key_list = [1, 2, 3]
        self.value_list = ['one', 'two', 'three']

    def get_keys(self):
        return self.key_list

    def get_values(self):
        return self.value_list

    def has_key(self,key):
        if key not in self.key_list:
            return False
        else:
            return True

    def get_value_of_key(self,key):
        if key in self.key_list:
            index = self.key_list.index(key)
            return self.value_list[index]
        else:
            raise Exception("key not exists")

d = custom_dict()
print(d.get_value_of_key(3))
#############################################################################
t = ([1,2],[3,4])
t[0].append(6)
print(t)
print(id(t))
############################################################################
def div_doc(div):
    def inner(a,b):
        if b > a:
            a,b = b,a
        return div(a,b)
    return inner

@div_doc
def div(a,b):
    return a/b

print(div(5,10))
#######################################################################

def pract(lst):
    print("inner-->",id(lst))
    # lst[2] = 55
    lst = (44,55)
    print("chaged_inner-->",id(lst))
    print(lst)

lst = (14,52,66,88)
# lst = 5
print("outer-->",id(lst))
print(lst)
##########################################################
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
    print("v-->",v)

    for row in m:
        print("row -->",row)
        for element in row:
            print("element -->",element)
            if v < element:
                v = element

    return v
print(fun(data[0]))

def f(i, values = []):
    values.append(i)
    print (values)
    return values

f(1,[5])
f(2)
f(3,[5])

init_tuple_a = 'a'
init_tuple_b = ('a', 'b')

print(type(init_tuple_a),type(init_tuple_b))
print (init_tuple_a == init_tuple_b)

l = [1, 2, 3]
init_tuple = ('Python',) * 3
print(init_tuple)