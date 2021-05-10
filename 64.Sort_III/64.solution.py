def inputTwoDimensionalTuple():
    t = input().split(';')
    L = []
    for i in t:
       L.append(tuple(map(int,i.strip("(").strip(")").split(","))))
    return L

L = inputTwoDimensionalTuple()
L.sort(key = lambda L:L[1])
print(L)
