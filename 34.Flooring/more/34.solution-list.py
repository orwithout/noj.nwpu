

def flooring2(n):
    if n%2 == 1 or n < 2:
        return 0
    f = [0 for i in range(n+1)]
    f[0] = 1
    f[2] = 3
    for i in range(4, n+1, 2):
        f[i] = f[i-2]*4 - f[i-4]
    return f[n]%100003



def flooring3(n):
    if n % 2 !=0 or n < 2:
        return 0
    else:
        fi = 1
        gi = 0
        hi = 0
        for i in range(2,n+1,2):
            Fi = 3*fi + gi + hi
            Gi = fi + gi
            Hi = fi + hi
            fi = Fi
            gi = Gi
            hi = Hi
        return fi%100003


for n in range(0,1001):
    print(flooring2(n),flooring2(n),flooring3(n))
