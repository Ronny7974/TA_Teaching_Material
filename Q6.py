a, b = map(int, input().split())
if a > b :
    a = a + b
    b = a - b
    a = a - b
for i in range(a, b + 1, 1):
    c = True
    if i < 2:
        continue
    for j in range(2, int(i ** 0.5) + 1, 1):
        if i % j == 0:
            c = False
            break
    if c : 
        print(i, end=' ')
print('')