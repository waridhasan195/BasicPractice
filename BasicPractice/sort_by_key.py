
lst = [[1, 2],[3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# lst.sort(key=lambda x: x[1])
# print(lst)


lst.sort(key=lambda x: x[1] + x[0])
print(lst)
