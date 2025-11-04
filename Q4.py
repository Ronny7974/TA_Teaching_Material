a = int(input())
toltal = 0
if a - 120 < 0:
    toltal += (a * 2.1)
    print(f"NT${toltal:.1f}")
elif a > 120 and a <= 500:
    toltal += 120*2.1
    toltal += (a - 120) * 3.02
    print(f"NT${toltal:.1f}")
else :
    toltal += 120 * 2.1
    toltal += (500 - 120) * 3.02
    toltal += (a - 500) * 4.39
    print(f"NT${toltal:.1f}")