
def sameBitsIs(bits):    # 0,1,5,6的任意次方，个位数仍然是 0,1,5,6
    sum = 1
    t = bits
    while True:
        t = t*bits %10
        sum += 1
        if t in (0,1,5,6):
            return sum,t

def powerBits(a,b):
    bits = a % 10
    r,t=sameBitsIs(bits)
    if b < r:
        t = 1
    for i in range(0,b%r):
        t = t*bits %10
    return t

a,b=map(int,input().split(' '))
while a>0 and b>0:
    print(powerBits(a,b))
    a,b=map(int,input().split(' '))

