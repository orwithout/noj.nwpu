
def floor(n):
    if n%2 == 1:
        return 0
    f = [0 for i in range(n+1)]
    f[0] = 1
    f[2] = 3
    for i in range(4, n+1, 2):
        f[i] = f[i-2]*4 - f[i-4]
    return f[n]%100003


def flooring(c1,c2,n):
    


n = int(input())
while n != 0:
    print(floor(n))
    n = int(input())

