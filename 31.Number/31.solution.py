# 本算法有误，例如输入99，得到285（99,99,87），正确应该是：295（97 + 99 + 99）
def number(n):
    for a1 in range(n, 0, -1):
        for a2 in range(n, 0, -1):
            if (a1+a2)%2 != 0:
                continue
            for a3 in range(n, 0, -1):
                if  (a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                    max = a1+a2+a3
                    return max

n = int(input())
print(number(n))


"""
正确算法：
def numberGrid1(n):
    max = (3 * n) // 5 * 5
    for t in range(max, -1, -5):
        for a2 in range(n, -1, -1):
            a3a = min(n, t - a2)
            for a3 in range(a3a, -1, -1):
                if (a2 + a3) % 3 == 0 and (t - a3) % 2 == 0 and (t - a2 - a3) <= n:
                    return t
"""
