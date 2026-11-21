#Q1
# names = "Python"
# scores = [95, 87, 92]
# tags = {"Python", "AI", "Beginner"}    -----unordered set
# print(names[1])
# print(scores[1])
# print(tags[1])





#Q2
# print(type("hello"))
# print(type([1, 2, 3]))
# print(type({1, 2, 3}))


#Q3
#block-A
# s = "hello"
# s[0] = "H"                   ---- Error stirings are immutable but lists are mutable
# print(s)



#block-B
# lst = [10, 20, 30]
# lst[0] = 99                   -----lists are mutable; strings are immutable; tuples are immutable
# print(lst)


#Q4

#--a
# print({1, 2, 2, 3, 3, 3})              -----{1, 2, 3}
# print([1, 2, 2, 3, 3, 3])              ------[1, 2, 2, 3, 3, 3]

#b
#print({101, 202, 101, 303, 202} )            -------{202, 101, 303}


#c
# s = {1, 2, 3}
# s.add(42)
# s.add("hello")             -------immutable datatypes are hashable
# s.add((10, 20))
# s.add([1, 2])                       ------because its mutable it cant be added



#e
# print(hash((1, 2, 3))) # ________ (works)
# print(hash((1, [2, 3]))) # ________ (what happens?)


#---------------------------------------------------------------------#
# list------ mutable ----non hashable
# str------immutable-------hashable

# tuple----immutable---hashable
#    |----mutable---non hashable

# set----mutable--------non hashable
#    |--elements of set are immutable-- hashable
#-------------------------------------------------------------------#


#Q5
# print('y' in "Python")
# print(87 in [95, 87, 92])
# print("AI" in {"Python", "AI", "Beginner"})
# print('z' in "Python")
# print(100 in [95, 87, 92])
# print("SQL" in {"Python", "AI", "Beginner"})


#Q8
# mixed = [42, "hello", True, 3.14, [1, 2, 3]]------------ list can have multiple data types
# print(len(mixed))
# print(type(mixed[0]))
# print(type(mixed[1]))
# print(type(mixed[4]))



#Q9
#a
# matrix = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# print(matrix[1][2])
# print(matrix[0][0])
# print(matrix[2][1])



# #b
# coords = {(0, 0), (1, 2), (3, 4), (1, 2)}              ------duplication is cancelled in set(deduplication)
# print(coords)
# print(len(coords))


#c
# article_tags = [
# {"Python", "AI"},
# {"Python", "Web"},
# {"AI", "ML"},
# ]
# print(article_tags[0])
# print("AI" in article_tags[1])
# print(len(article_tags))


#d
# data = [
# ("Alice", {95, 87, 92}),           --------tuple in list
# ("Bob", {78, 85, 90}),
# ]
# print(data[0][0])
# print(data[1][1])
# print(88 in data[0][1])
