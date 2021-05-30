a=input()
l=len(a)-a.index(".")-1
mu=10**l
zi=eval(a)*mu
def Euclidean(a, b):
    ma = max(a,b)
    mi = min(a,b)
    if ma%mi==0:        
        return(mi)
    else:
        return Euclidean(mi, ma%mi)
k=Euclidean(zi,mu)
print(int(zi/k),'/',int(mu/k),sep='')

