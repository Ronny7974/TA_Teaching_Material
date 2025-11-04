a = input()
tol = 0
for i in a:
    tol += int(i)
print(f"Pass 1 : {tol}")
c = 2
while tol > 10 :
    b = str(tol)
    tol = 0
    for i in b:
        tol += int(i)
    print(f"Pass {c} : {tol}")
    c += 1
print(f"Digital Root of {a} : {tol}")    