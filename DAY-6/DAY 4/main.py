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
#     print("Tail")




# python list
exciting_moment = ["Brainy", "Airly", "Beezeway", "Prosepr", "Alex", "Adaaku", "Pistis", "Abigail", "Silas"]
exciting_moment[3] = "Prosper"
exciting_moment.append("Ankrah")
exciting_moment.remove("Silas")
print(exciting_moment)




# bill payment🤣🤣🤣😍


# import random
# names_string = input("Enter, names of friends present at the table separated by a comma.\n")
# names = names_string.split(", ")
#
# # count the number of list items in "names" and assign it to num_of_names
# num_of_names = len(names)
#
# # generate a random number b/n 0 and the last index
# random_intname = random.randint(0, num_of_names - 1)
# person_who_will_pay = names[random_intname]
# # print(random_intname)
#
# # or person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today!")




# # dirty_dozen = ["goat", "kofi", "ama", "cat", "dog"]
# humans = ["koif", "ama"]
# animals = ["goat", "dog", "cat"]
# dirty_dozen = [humans, animals]
# print(dirty_dozen)



# row1 = ["😍","😍","😍"]
# row2 = ["😍","😍","😍"]
# row3 = ["😍","😍","😍"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure\n")
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")
# # print(map)




# project(rock paper scissors)
# import random
# human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# rocks = "Rock"
# papers = "Paper"
# scissorss = "Scissors"
#
# # human_option = [rock, paper, scissors]
# print("Human selection:")
# if human == 0:
#     print(rocks)
# elif human == 1:
#     print(papers)
# elif human == 2:
#     print(scissorss)
# else:
#     print("You've entered a wrong number. Play again!")
#
#
#
# rock = "Rock"
# paper = "Paper"
# scissors = "Scissors"
#
# print("Computer selction:")
# computer_option = [rock, paper, scissors]
# random_int = random.randint(0, 2)
# computer_selection = computer_option[random_int]
# print(computer_selection)
#
# if (computer_selection == paper) and (human == 0):
#     print("You lose! Computer won")
# elif (computer_selection == rock) and (human == 2):
#     print("You lose! Computer won")
# elif (computer_selection == scissors) and (human == 1):
#     print("You lose! Computer won")
# elif (computer_selection == rock) and (human == 1):
#     print("You won!")
# elif (computer_selection == scissors) and (human == 0):
#     print("You won!")
# elif (computer_selection == paper) and (human == 2):
#     print("You won!")
# else:
#     print("Draw! Play again.")
#





# angela's own

import random

rock = "✊✊"
paper = "✋✋"
scissors = "✌✌"

game_images = [rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if human >= 3 or human < 0:
    print("You've entered a wrong number. You lose!")
else:
    print(game_images[human])

    computer_choice = random.randint(0, 2)
    print(f"computer chose:\n{game_images[computer_choice]}")
    # print(game_images[computer_choice])
    if (computer_choice == 1) and (human == 0):
        print("You lose!")
    elif (computer_choice == 0) and (human == 2):
        print("You lose!")
    elif (computer_choice == 2) and (human == 1):
        print("You lose!")
    elif (computer_choice == 0) and (human == 1):
        print("You won!")
    elif (computer_choice == 2) and (human == 0):
        print("You won!")
    elif (computer_choice == 1) and (human == 2):
        print("You won!")
    else:
        print("Draw! Play again.")
