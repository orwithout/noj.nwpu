
def isPhoneNumber2(s,dd):
    for d in dd:
        if len(s)==11 and s.isdigit() and s[:2]==d:
            return True
    return False
        

s=input()
dd = ["13","14","15","17","18","19"]
while s!="":
    print(isPhoneNumber2(s,dd))
    s=input()
