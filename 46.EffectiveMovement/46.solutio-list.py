
def EffectiveMovement(x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        return True
    if x1>x2 or y1>y2:
        return False
    return EffectiveMovement(x1+y1,y1,x2,y2) or EffectiveMovement(x1,y1+x1,x2,y2)

x1,y1,x2,y2 = map(eval,input().split())
if x1>0 or y1>0 or x2>0 or y2>0:
    print(str(EffectiveMovement(x1,y1,x2,y2)).lower())
