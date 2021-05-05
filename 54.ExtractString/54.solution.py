
def extractStr(s):
    if len(s)<2:
        return s
    return s[:2] + s[-2:]

s=input()
while s !="":
    print(extractStr(s))
    s=input()
