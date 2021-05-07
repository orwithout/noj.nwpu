
def FormulaCalc(s,pp):
    if len(s)==3 and len(pp)==2:
        if s[1]=='+':
            pp[0] = pp[0] + pp[1]
            return s[2:],pp[:1]
        if s[1]=='-':
            pp[0] = pp[0] - pp[1]
            return s[2:],pp[:1]
        if s[1]=='*':
            pp[0] = pp[0] * pp[1]
            return s[2:],pp[:1]
        if s[1]=='/':
            pp[0] = pp[0] / pp[1]
            return s[2:],pp[:1]
        if s[1]=='%':
            pp[0] = pp[0] % pp[1]
            return s[2:],pp[:1]

    if len(s)==4 and len(pp)==2:
        if s[1] == s[2] =='*':
            pp[0]=pp[0]**pp[1]
            return s[3:],pp[:1]
        if s[1] == s[2] =='/':
            pp[0]=pp[0]//pp[1]
            return s[3:],pp[:1]

    if len(s)>=5 and len(pp)>=3:
        if s[1]=='+' and (s[3]=='+' or s[3]=='-'):
            pp[0] = pp[0] + pp[1]
            return s[2:],pp[:1] + pp[2:]
        if s[1]=='-' and (s[3]=='+' or s[3]=='-'):
            pp[0] = pp[0] - pp[1]
            return s[2:],pp[:1] + pp[2:]
        if s[1]=='*' and s[2]!='*' and (s[3]=='+' or s[3]=='-' or s[3]=='/' or s[3]=='%' or (s[3]=='*' and s[4] != '*')):
            pp[0] = pp[0] * pp[1]
            return s[2:],pp[:1] + pp[2:]
        if s[1]=='/' and s[2]!='/' and (s[3]=='+' or s[3]=='-' or s[3]=='/' or s[3]=='%' or (s[3]=='*' and s[4] != '*')):
            pp[0] = pp[0] / pp[1]
            return s[2:],pp[:1] + pp[2:]
        if s[1]=='%' and (s[3]=='+' or s[3]=='-' or s[3]=='/' or s[3]=='%' or (s[3]=='*' and s[4] != '*')):
            pp[0] = pp[0] % pp[1]
            return s[2:],pp[:1] + pp[2:]
        if s[1]=='+' or s[1]=='-' or (s[1]=='*' and s[2]!='*') or (s[1]=='/' and s[2]!='/') or s[1]=='%':
            st,ppt = FormulaCalc(s[2:],pp[1:])
            return s[:2] + st,pp[:1] + ppt

    if len(s) >=6 and len(pp)>=3:
        if s[1] == s[2] =='*':
            pp[0] = pp[0]**pp[1]
            return s[3:],pp[:1] + pp[2:]
        if s[1] == s[2] =='/' and (s[4]=='+' or s[4]=='-' or s[4]=='/' or s[4]=='%' or (s[4]=='*' and s[5] != '*')):
            pp[0] = pp[0]//pp[1]
            return s[3:],pp[:1] + pp[2:]
        if s[1] == s[2] =='/':
            st,ppt = FormulaCalc(s[3:],pp[1:])
            return s[:3] + st,pp[:1] + ppt

t=s=input()
pp=list(map(eval,input().split()))
while len(s)>=3 and len(pp)>=2:
    s,pp = FormulaCalc(s,pp)
t = t+"="+str(pp[0])
print(t)


