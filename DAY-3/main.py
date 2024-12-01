





# challenge
# coding exercise
# number = int(input("Enter the number you want to check!\n"))

# if number % 2 == 0 :
#     print("The numebr is an even number.")
# else:
#     print("The number is an odd number.")


# EXX
# print("Hello welcome to my BMI calculator")
#
# height = float(input("enter your height in m:\n"))
# weight = float(input("enter your weight in kg:\n"))
#
# BMI = round(weight / height **2)
#
# if BMI < 18.5:
#     print(f"Your BMI is {BMI},you are underweight")
# elif BMI < 25:
#     print(f"Your BMI is {BMI},you have normal weight")
# elif BMI < 30:
#     print(f"Your BMI is {BMI},you are overweight")
# elif BMI < 35:
#     print(f"Your BMI is {BMI},you are obese")
# else:
#     print(f"Your BMI is {BMI},you are clinically obese")



# leap year challenge

# print("Welcome to my leap year detector")
# year = int(input("Enter the year! "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")







# print("Welcome to Python Pizza Deliveries")
#
# size = input("what size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
#
#
# bill = 0
# # when the user selects small(S)
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
#     if add_pepperoni == "Y":
#         if size == "S":
#             bill += 2
#         else:
#             bill += 3
#
#             if extra_cheese == "Y":
#                 bill += 1
#
# print(f"Your final bill is ${bill}")












# logical operator

# print("WELCOME TO THE LOVE CALCULATOR")
# name1 = input("What is your name? ")
# name2 = input("what is his/her name? ")
#
# # counting of letters in combine_names corresponding to "TRUE".
# combine_names = name1 + name2
# lower_case_name = combine_names.lower()
# countT = int(lower_case_name.count("t"))
# countR = int(lower_case_name.count("r"))
# countU = int(lower_case_name.count("u"))
# countE = int(lower_case_name.count("e"))
#
# sum_count_true = countU + countE + countR + countT
#
# # counting of letters in combine_names corresponding to "LOVE".
# countL = int(lower_case_name.count("l"))
# countO = int(lower_case_name.count("o"))
# countV = int(lower_case_name.count("v"))
# countE = int(lower_case_name.count("e"))
#
# sum_count_love = countL + countO + countV + countE
#
#
# love_score = str(sum_count_true) + str(sum_count_love)
# new_love_score = int(love_score)
#
# if (new_love_score < 10) or (new_love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (new_love_score >= 40) and (new_love_score <= 50):
#     print(f"Your score is {new_love_score}, you are alright together.")
# else:
#     print(f"Your score is {new_love_score}.")








# treasure iland
# print("Welcome to Treasure Island.")
# print("Your mission is to find the hidden treasure.")
#
# cross_road = input('You\'re at a cross road. Where do you want to pass? Type "Left" "Right\n"')
# lower_cross_road = cross_road.lower()
#
# if lower_cross_road == "left":
#     lake_side = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n')
#     lower_lake_side = lake_side.lower()
#     if lower_lake_side == "wait":
#         house = input("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you want to choose?\n")
#         lower_house = house.lower()
#         if lower_house == "blue":
#             print("Congratulations, you won.")
#         elif lower_house =="yellow":
#             print("It's a room full of fire. Game Over.")
#         elif lower_house == "red":
#             print("A room of beasts, Game Over.")
#         else:
#             print("You an unexisting door. Game Over.")
#     else:
#         print("Game Over, the shark ate you up.")
# else:
#     print("Game Over, you fell into a hole.")








# import random
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)







# import random
#
# random_integer = random.randint(1, 4)
# if (random_integer == 1) or (random_integer == 2):
#     print("Head")
# else:
#     print("Tail"




# python list
# exciting_moment = ["Brainy", "Airly", "Beezeway", "Prosepr", "Alex", "Adaaku", "Pistis", "Abigail", "Silas"]
# exciting_moment[3] = "Prosper"
# exciting_moment.append("Ankrah")
# exciting_moment.remove("Silas")
# print(exciting_moment)




# bill payment🤣🤣🤣😍😍


import random

names_string = input("Enter names of friends present at the table separated by a comma.\n")
names = names_string.split(", ")
num_of_names = len(names)

random_intname = random.randint(0, num_of_names - 1)
person_who_will_pay = names[random_intname]
print(random_intname)

print(person_who_will_pay + "is going to buy the meal today!")
