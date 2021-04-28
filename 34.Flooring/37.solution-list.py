


def sameBitsIs(bits):    # 1,5,6的任意次方，个位数仍然是 1,5,6
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
    if b < 0:
        return 0
    elif b==0:
        return 1
    elif b < r:
        t = 1
    for i in range(0,b%r):
        t = t*bits %10
    return t

for a in range(0,100):
    for b in range(0,100):
        c = a**b
        d = powerBits(a,b)
        #if c%10 - d !=0:
        print(a,b,c,d)


