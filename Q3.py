a = int(input())
if a % 4 == 0 and a % 100 != 0 :
    print(f"{a} : Leap Year")
elif a % 400 == 0:
    print(f"{a} : Leap Year")
else :
    print(f"{a} : Not a Leap Year")