a = int(input())
b = int(input())
GCD = 0
i = 1
if a == 0 or b == 0:
    print(max(a,b))
else:

    while i <= min(a,b):
        if a % i == 0 and b % i == 0:
            GCD = i
        i += 1
    print(GCD)