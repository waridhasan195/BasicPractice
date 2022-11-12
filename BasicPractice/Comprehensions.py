

# x = [0 for i in range((100)+1)]
# print(x)

# x = [i for i in range((100)+1)]
# print(x)

# x = [i for i in range(100) if i%2 == 0]
# print(x)


# x = [i+j for i in range(10) for j in range(10)]
# print(x)

# x = [[_ for _ in range(5)] for _ in range(5)]
# print(x)

# x = (i for i in "Hello")
# print(tuple(x))


sentence = "Hello my name is warid"
sett = set(sentence)
print(sett)
x = {char: sentence.count(char) for char in set(sentence)}
print(x)





