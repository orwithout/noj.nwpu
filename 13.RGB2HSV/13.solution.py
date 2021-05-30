R=eval(input())/255
G=eval(input())/255
B=eval(input())/255
V=max(R,G,B)
ma=V
mi=min(R,G,B)
if V==0:
    S=0
else:
    S=(ma-mi)/ma
if ma==R:
    H=(G-B)/(ma-mi)
elif ma==G:
    H=2+(B-R)/(ma-mi)
else:
    H=4+(R-G)/(ma-mi)
H*=60
if H<0:
    H+=360
S*=100
V*=100
print('%.4f'%H,end=',')        
print('%.4f'%S,end='%,')
print('%.4f'%V,end='%')
