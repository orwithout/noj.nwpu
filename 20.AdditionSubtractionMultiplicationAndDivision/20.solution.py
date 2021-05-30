def Euclidean(a, b):
    ma = max(a,b)
    mi = min(a,b)
    if ma%mi==0:        
        return(mi)
    else:
        return Euclidean(mi, ma%mi)
def fenshuhuajian(a,b):
    chu=Euclidean(a,b)
    return a/chu,b/chu
m=eval(input())
n=eval(input())
p=eval(input())
q=eval(input())
#+
zi=m*q+n*p
mu=n*q
zi,mu=fenshuhuajian(zi,mu)
print("(%d/%d)+(%d/%d)=%d/%d"%(m,n,p,q,zi,mu))
#-
zi=m*q-n*p
mu=n*q
zi,mu=fenshuhuajian(zi,mu)
print("(%d/%d)-(%d/%d)=%d/%d"%(m,n,p,q,zi,mu))
#*
zi=m*p
mu=n*q
zi,mu=fenshuhuajian(zi,mu)
print("(%d/%d)*(%d/%d)=%d/%d"%(m,n,p,q,zi,mu))
#/
zi=m*q
mu=n*p
zi,mu=fenshuhuajian(zi,mu)
print("(%d/%d)/(%d/%d)=%d/%d"%(m,n,p,q,zi,mu))
