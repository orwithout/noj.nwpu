def operands(n):
    op = 0
    m = sum(list(map(int, list(str(n)))))
    while n >= m != 0:
        op += 1
        n -= m
        m = sum(list(map(int, list(str(n)))))
    return op

#for i in range(1,100):
n=int(input())
print(operands(n))


