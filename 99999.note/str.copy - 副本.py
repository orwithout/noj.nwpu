# https://juejin.cn/post/6844903670316793864
# 函数传参，list默认是指针
# 如果传递 nn+[],会变为copy
n=10
a = [[1,2],[2,3],[1]]
b = [1,2]
    
c =list(set(a)-set([1,2,3]))
