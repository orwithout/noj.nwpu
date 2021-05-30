a=input()
b=eval(input())-1
qian=a[:b]
hou=[]
for i in a[b:]:
    if ord(i)>95:
        hou.append(chr(219-ord(i)))
    else:
        hou.append(chr(155-ord(i)))
hou=''.join(hou)
print(qian+hou)
