
# Probelm 1
students = ['John', 'Emily', 'Jessica', 'Michael']
print("Exercise 1: ", students[1], students[-1]) # second student's name


# Problem 2
students = ['John', 'Emily', 'Jessica', 'Michael']
foods = ('pizza', 'pasta', 'salad', 'sushi')

for i in range(len(students)):
    print("Exercise 2: ", f"{foods[i]} goes here is a good food")


# Problem 3
foods = ('pizza', 'pasta', 'salad', 'sushi')
for i in range(-2,0):
    print("Exercise 3: ", foods[i])

# Problem 4
home_town = {'city': 'Houston', 'state': 'Texas', 'population': 2300000}
print("Exercise 4: ", f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Problem 5
home_town = {'city': 'Houston', 'state': 'Texas', 'population': 2300000}

for key, value in home_town.items():
    print("Exercise 5: ", f"{key} = {value}")


# Problem 6
students = ['John', 'Emily', 'Jessica', 'Michael']
cohort = []

for student in students:
    student_info = {'student': student, 'fav_food': 'Cheeseburger'}
    cohort.append(student_info)

for student in cohort:
    print("Exercise 6: ", student)

# Problem 7
students = ['John', 'Emily', 'Jessica', 'Michael']
awesome_students = [f"{student} is awesome!" for student in students]

for student in awesome_students:
    print("Exercise 7: ", student)

# Problem 8
for food in (food for food in foods if 'a' in food):
    print("Exercise 8: ", food)