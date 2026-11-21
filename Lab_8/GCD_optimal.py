a = int(input())
b = int(input())
limit = min(a,b)
gcd = 0
i = limit
if a == 0 or b == 0:
    print(max(a,b))
else:

    while i >= 0:
        if a % i == 0 and b % i == 0:
            gcd = i
            break
        i -= 1
    print(gcd)

