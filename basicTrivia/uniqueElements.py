def unique(list):
    size = len(list)
    map = {}
    newlist = []
    for element in list:
        if element not in map:
            newlist.append(element)
            map[element] =  1
    return newlist


#Driver code

mylist = [1,1,1,1,2,2,3,4]
print(unique(mylist))
