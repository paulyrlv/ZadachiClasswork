s = str(input())
n = int(input())
count = len(s)
for i in range(n, count):
    print(s[i], end='', sep='')
for i in range(n):
    print(s[i], end='', sep='')
