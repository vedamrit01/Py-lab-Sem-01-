


m=[[1,2,3],[4,5,6],[7,8,9]]


#TRANSVERE FOUND BY MISTAKE

# columns=[]
# i=0
# while i<len(m[0]):
#     j=0
#     ci=[]
#     while j < len(m):
#         ci.append(m[j][i])
#         j+=1
#     columns.append(ci)
#     i+=1
# print(columns)

#row transversal

# i=0
# total=0
# while i<len(m):
#     j=0
#     while j<len(m[i]):
#         print(m[i][j] , end=" ")
#         total+=m[i][j]
#         j+=1
#     print()
#     i+=1

# print(f"Total: {total}")


rows_sum=[]
column_sum=[]
i=0
while i<len(m):
    j=0
    r_sum=0
    while j<len(m[i]):
        r_sum+=m[i][j]
        j+=1
    rows_sum.append(r_sum)
    i+=1

print(rows_sum)


j=0
while j<len(m):
    i=0
    c_sum=0
    while i<len(m):
        c_sum+=m[i][j]
        i+=1
    column_sum.append(c_sum)
    j+=1

print(column_sum)
