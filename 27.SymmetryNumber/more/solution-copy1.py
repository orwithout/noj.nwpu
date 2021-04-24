def len_n(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
        #print(n)
    #print(count)
    return count

def find(m):
    n = len_n(m)
    nums = n % 2 * list('018') or ['']
    print("nums1:",nums)
    while n > 1:
        n -= 2
        nums = [a + num1+ b for a, b in '00 11 88 69 96'.split()[n < 2:] for num1 in nums]
        print("nums2:",nums)
    if str(m) in nums:
        return print("Yes")
    else:
        return print("No")
    
for i in range(1,100):
    num = int(input())
    find(num)
