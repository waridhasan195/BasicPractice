

name = ['sakib', 'tamim', 'roy', 'mahmudullah']
ages = [25, 32, 21, 38]
eye_color = ['black', 'brown', 'blue', 'red', 'unknown']

# print(list(zip(name, ages, eye_color)))


for name, age, eye_color in zip(name, ages, eye_color):
    if age > 25:
        pass
    print(name)
    print(age)
    print(eye_color)
    print("---------------------")


   
