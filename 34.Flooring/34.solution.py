
def flooring(n):
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


n = int(input())
while 1<= n <=1000:
    print(flooring(n))
    n = int(input())
