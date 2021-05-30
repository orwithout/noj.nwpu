aa = input().split()
tt = list()
for s in aa:
    if s[:8] =='https://' or s[:7] =='http://' or s[:7] =='file://' or s[:6] =='ftp://':
        tt = tt + [s.rstrip(',').rstrip('.').rstrip(';').rstrip(':').rstrip('!')]
print(tt)
