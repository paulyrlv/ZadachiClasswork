s = str(input())
s = s.lower()
s = s.replace(' ', '')
count = len(s)
k = 0
if count % 2 != 0:
    print(0)
else:
    for i in range(count // 2):
        if s[i-1] == s[-i]:
            k += 1
    if k * 2 == count:
        print(1)
    else:
        print(0)
