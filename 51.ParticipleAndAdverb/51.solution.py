
def ParticipleAndAdverb(s):
    if len(s)<3:
        return s
    if s[-3:] == "ing":
        return s+"ly"
    return s + "ing"

s=input()
while s!="":
    print(ParticipleAndAdverb(s))
    s=input()
