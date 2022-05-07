# xndir 1
def creat (start1, stop, step):
    listReturn = [start1]
    for i in range(start1+1, stop, step):
        listReturn.append(i)
    return listReturn

# print(creat (1, 25, 2))