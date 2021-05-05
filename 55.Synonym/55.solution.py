import re
def synonym(s):
    for i in range(0,len(s)-6):
        if s[i:i+3]=="not":
            for j in range(i+3,len(s)-3):
                if s[j:j+4]=="poor":
                    return s[:i] + "good" + s[j+4:]
    return s
                    

s=input()
while s !="":
    print(synonym(s))
    s=input()
