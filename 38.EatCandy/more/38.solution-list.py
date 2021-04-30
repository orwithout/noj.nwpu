
def eatCandyPlans(n):
    if n<=2:
        return n
    else:
        return eatCandyPlans(n-1) + eatCandyPlans(n-2)


def eatCandyPlans2(n):
    if n<=2:
        return n
    p_1 = 2
    p_2 = 1
    for i in range(3,n+1):
        pi = p_1 + p_2
        p_2 = p_1
        p_1 = pi
    return p_1
        



"""
n = int(input())
while n > 0:
    print(eatCandyPlans(n))
    n = int(input())
"""

for n in range(0,1001):
    #print(eatCandyPlans3(n))
    print(eatCandyPlans(n),eatCandyPlans2(n))
