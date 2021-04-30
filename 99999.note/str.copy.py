# https://juejin.cn/post/6844903670316793864
# 函数传参，list默认是指针
# 如果传递 nn+[],会变为copy
def EqualPlans(nn):
    nn += "addin func"
    return nn


ss = '1123456'
print(ss)
fnn=EqualPlans(ss)
ss += "nn"

print(fnn)
print(ss)
