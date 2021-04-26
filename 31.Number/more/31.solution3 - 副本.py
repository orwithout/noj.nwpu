def numberGrid(n):
    max = (3 * n) // 5 * 5
    for t in range(max, -1, -5):
        for a2 in range(n, -1, -1):
            a3a = min(n, t - a2)
            for a3 in range(a3a, -1, -1):
                if (a2 + a3) % 3 == 0 and (t - a3) % 2 == 0 and (t - a2 - a3) <= n:
                    return t


#for i in range(0,101):
n=int(input())
if 0<=n<=100:
    print(numberGrid(n))
