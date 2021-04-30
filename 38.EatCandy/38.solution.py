
def eatCandyPlans(n):
    if n<=2:
        return n
    p_1 = 2
    p_2 = 1
    for i in range(3,n+1):
        pi = p_1 + p_2
        p_2 = p_1
        p_1 = pi
    return p_1


n = int(input())
while n > 0:
    print(eatCandyPlans(n))
    n = int(input())
