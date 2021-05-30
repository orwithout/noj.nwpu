a=input()
n=eval(input())
l=a.split(' ',-1)
hou=l[:n]
qian=l[n:]
rever=qian+hou
print(" ".join(str(i) for i in rever))
