import operator


def activity_selection(actvity_info):
    actvity_info.sort(key=operator.itemgetter('f'), reverse=False)
    print(actvity_info)
    print(actvity_info[0]['a'])
    i = 0
    for j in range(1,len(actvity_info)):
        if actvity_info[i]['f']<=actvity_info[j]['s']:
            print(actvity_info[j]['a'])
            i=j


activit_dict = [
{'a' : 'B','s':3,'f':4},
{'a' : 'C','s':0,'f':6},
{'a' : 'E','s':8,'f':9},
{'a' : 'F','s':5,'f':9},
{'a' : 'A','s':1,'f':2},
{'a' : 'D','s':5,'f':7},

]
activity_selection(activit_dict)