def symmetry(aInt):
    aStr=str(aInt)
    n=len(aStr)
    for i in range(0,n):
        if aStr[i]+aStr[n-i-1] not in ['00','11','88','96','69']:
            return "Not"
        elif n-i-1-i<=1:
            return "Yes"

aInt=int(input())
print(symmetry(aInt))
