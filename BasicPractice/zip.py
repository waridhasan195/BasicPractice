

name = ['sakib', 'tamim', 'roy', 'mahmudullah', 'Mehedi']
ages = [25, 32, 21, 38, 19]
eye_color = ['black', 'brown', 'blue', 'red', 'Unknown', 'Unknown']

# print(list(zip(name, ages, eye_color)))


# for name, age, eye_color in zip(name, ages, eye_color):
#     if age > 25:
#         pass
#     print(name)
#     print(age)
#     print(eye_color)
#     print("---------------------")


print(list(zip(name, ages, eye_color)))

for name, age, eye_color in zip(name, ages, eye_color):
    if age > 20:
        pass
    print(f"Name: {name},\tAge: {age},\tEye Color: {eye_color}")
    
