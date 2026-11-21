r,c = map(int,input().split())
i = 0
m = []
while i < r:
    row = list(map(int,input().split()))
    m.append(row)
    i += 1
top = 0
bottom = r - 1
left = 0
right = c - 1

while top <= bottom and left <= right:
    # Top Row traversal
    j = left
    while j <= right:
        print(m[top][j], end = " ")
        j += 1
    # Right column traversal
    i = top
    while i <= bottom:
        print(m[i][right], end = " ")
        i += 1
    # Bottom Row traversal
    j = right
    while j >= left:
        print(m[bottom][j])





    
