users = ['Bob', 'Tom', 'Ken']
int_numbers = [i for i in range(1, 6)]
kazuma_info = ['Kazuma', 'Takahashi', 35]
members = ["Kazuma", "Makoto", "Ohira"]
print(members[1])
print(members[0])
print(f"Name: {kazuma_info[1]} {kazuma_info[0]}, Age: {kazuma_info[2]}")

odd_numbers = [1, 3, 5, 7, 9]
[print(i) for i in odd_numbers]
even_numbers = [2, 4, 6, 8]
[print(i * 2) for i in even_numbers]
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

sentences = list(map(lambda list: f'Name: {list[0]}, Age: {list[1]}', users_info))
[print(i) for i in sentences]

kazuma_info = {'first_name': 'Kazuma', 'family_name': 'Takahashi', 'age': '35'}

print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35

import random

print(random.randint(1, 6))

height, weight = float(input("Height(m)? >")), float(input("Weight(kg)? >"))
print(f"Your BMI is {round(weight / (height**2), 2)}")