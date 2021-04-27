
def changan(hi,hj,pi,pj,bi,bj):    # hi<=pi bi , hj<=pj bj
    if (hi==pi and hj==pj) or (hi==bi and hj==bj):
        return 0
    elif (hi==bi-1 and hj==bj) or (hi==bi and hj==bj-1):
        return 1
    elif (hi<bi-1 and hj==bj):
        return changan(hi+1,hj,pi,pj,bi,bj)
    elif (hi==bi and hj<bj-1):
        return changan(hi,hj+1,pi,pj,bi,bj)
    elif (hi<=bi-1 and hj<=bj-1):
        return changan(hi+1,hj,pi,pj,bi,bj) + changan(hi,hj+1,pi,pj,bi,bj)
    else:
        print("error:",hi,hj,pi,pj,bi,bj)
        exit(1)



# a!/(a-n)!
def factorial(n, a):
        pro = 1
        tmp = n
        for i in range(a):
            pro *= tmp
            tmp -= 1
        return pro
# b!/a!*(b-a)!
def c(a, b):
    return factorial(a+b, a)/factorial(a, a)
def cout(bx, by, px, py):
    if px <= bx and py <= by:
        return c(bx, by) - c(px, py)*c(bx-px, by-py)
    else:
        return c(bx, by)



for bi in range(0,15):
    for bj in range(0,15):
        for pi in range(0,bi):
            for pj in range(0,bj):
                a1 = changan(0, 0, pi, pj, bi, bj)
                a2 = int(cout(bi, bj, pi, pj))
                if a1 != a2:
                    print(pi,pj,bi,bj,":",a1,a2,"   ",a1-a2)


