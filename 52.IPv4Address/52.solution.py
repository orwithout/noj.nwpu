
def isIPv4(s):
    nn=s.split(".")
    for i in range(len(nn)):
        if (not nn[i].isdigit()) or int(nn[i])<0 or int(nn[i])>255 or i>3:
            return False
    if int(nn[0])==0:
        return False
    return True

s=input()
while s!="":
    print(isIPv4(s))
    s=input()
