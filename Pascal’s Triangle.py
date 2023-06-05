#Generating pascal's triangle
def GenPascalTriangle(n : int):
    lst = []
    for x in range(n):
        lst.append([1])
        if x > 1:
            for c in range(x-1):
                lst[x].append(lst[x-1][c]+lst[x-1][c+1])
        if x > 0:
            lst[x].append(1)
    return lst
