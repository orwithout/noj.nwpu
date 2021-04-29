
MAX = 1001
s = [i for i in range(MAX)]
n = int(input())
s[0]=1
s[2]=3
for i in range(4, MAX, 2):
    s[i]=4*s[i-2]-s[i-4]
while n>0:
    if n&1:
        print(0)
    else:
        print(s[n]%100003)
    n = int(input())
