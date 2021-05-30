# 使用十二小时制的系统通常将“正午”以“12:00 p.m.”表示，而“午夜”为则被标为“12:00 a.m.”，习惯使用二十四小时制的人可能会对此产生理解错误。

list=input().split(' ')
if list[1]=='AM':
    if list[0][0:2] == '12':
        list[0] = '00' + list[0][2:]
elif list[1]=='PM':
    if list[0][0:2] != '12':
        list[0] = str(int(list[0][0:2])+12) + list[0][2:]
print(list[0])
