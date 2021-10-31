def checkerBoard(x,y):
    result = []
    for i in range(0,x):
        temp=[]
        for j in range(0,y):
            temp.append((i+j) % 2)
        result.append(temp)
    return result

rowss = checkerBoard(4,4)


for row in rowss:
    print(rowss)