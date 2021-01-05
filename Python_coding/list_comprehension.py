# size = int(input("enter size:"))
# li = []
# for i in range(size):
#     li.append(int(input()))

even_nos = [ele for ele in range(0, 21, 2)]
odd_nos = [ele for ele in range(1, 21, 2)]
print("Even numbers in the list: ", even_nos,odd_nos)
z = 0
for x,y in zip(even_nos,odd_nos):
    z += x*y

