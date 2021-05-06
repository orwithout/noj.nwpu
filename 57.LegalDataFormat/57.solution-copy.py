import time
def isLegalDataFormat(x):
    if x == "":
        return False
    else:
        try:
            if "-" in x:
                time.strptime(x,"%Y-%m-%d")
                return True
            elif "." in x:
                time.strptime(x,"%Y.%m.%d")
                return True
            elif "/" in x:
                time.strptime(x,"%Y/%m/%d")
                return True
            else:
                return True
        except:
            return False


def isLegalDataFormat2(s,dd):
    for d in dd:
        tt = s.split(d)
        if len(tt)==3:
            if tt[0].isdigit() and tt[1].isdigit() and tt[2].isdigit():
                if 0<int(tt[0])<=9999:
                    if (int(tt[1])==1 or int(tt[1])==3 or int(tt[1])==5 or int(tt[1])==7 or int(tt[1])==8 or int(tt[1])==10 or int(tt[1])==12) and 0<=int(tt[2])<=31:
                        return True
                    elif (int(tt[1])==4 or int(tt[1])==6 or int(tt[1])==9 or int(tt[1])==11) and 0<=int(tt[2])<=30:
                        return True
                    elif int(tt[1])==2 and 0<=int(tt[2])<=28:
                        return True
    return False
        


s=input()
while s!="":
    dd = ["-","/","."]
    print(isLegalDataFormat(s),isLegalDataFormat2(s,dd))
    s=input()
