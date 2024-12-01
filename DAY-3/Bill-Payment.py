import random

names_string = input("Enter names of friends present at the table separated by a comma.\n")
names = names_string.split(", ")
num_of_names = len(names)

random_intname = random.randint(0, num_of_names - 1)
person_who_will_pay = names[random_intname]
print(random_intname)

print(person_who_will_pay + "is going to buy the meal today!")
