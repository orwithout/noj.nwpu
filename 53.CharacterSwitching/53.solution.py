
def characterSwitching(s):
    for i in range(0,len(s)):
        if s[i]==",":
            s = s[:i] + '.'+s[i+1:]
        elif s[i]==".":
            s = s[:i] + ','+s[i+1:]
    return s

s=input()
print(characterSwitching(s))

