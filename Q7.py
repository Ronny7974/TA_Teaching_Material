a = input().split(' ')
b = input()
p = 0
print(ord('A'), ord('Z'), ord('a'), ord('z'))
for i in range(0, len(b), 1):
    if b[i] == ' ':
        print(' ', end = '')
        continue
    t = ord(b[i])
    if t <= 90 and t >= 65:
        t -= int(a[p])
        p += 1
        if t < 65:
            t = 90 - (65 - t) + 1
    elif t >= 97 and t <= 122:
        t -= int(a[p])
        p += 1
        if t < 97:
            t = 122 - (97 - t) + 1
    if p >= len(a):
        p = p - len(a)
    print(chr(t), end = '')
