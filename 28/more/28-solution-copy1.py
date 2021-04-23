# https://blog.csdn.net/weixin_43520256/article/details/109137366

def isPalindrome(n):
    temp1 = n
    temp2 = 0
    while temp1 > 0:
        temp2 = temp1 % 10 + temp2 * 10
        temp1 //= 10
    if n == temp2:
        return True
    else:
        return False

num = int(input())
if isPalindrome(num):
    print("Yes")
else:
    print("Not")
