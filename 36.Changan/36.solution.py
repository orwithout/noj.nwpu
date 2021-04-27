
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

    
bi,bj,pi,pj=map(int,input().split(','))
while bi>=0 and bj>=0 and pi>=0 and pj>=0:
    print(changan(0,0,pi,pj,bi,bj))
    bi,bj,pi,pj=map(int,input().split(','))

