# https://juejin.cn/post/6844903670316793864
# 函数传参，list默认是指针
# 如果传递 nn+[],会变为copy
def EqualPlans(nn):
    nn += ["addin func"]
    nn[0]=999
    return nn


nn = [1,1]
print(nn)
fnn=EqualPlans(nn+[1000])
nn += [111]

print(fnn)
print(nn)
