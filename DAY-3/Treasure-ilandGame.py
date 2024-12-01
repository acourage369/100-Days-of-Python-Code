
# treasure iland
print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")

cross_road = input('You\'re at a cross road. Where do you want to pass? Type "Left" "Right\n"')
lower_cross_road = cross_road.lower()

if lower_cross_road == "left":
    lake_side = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                      'Type "Wait" to wait for a boat. Type "Swim" to swim across.\n')
    lower_lake_side = lake_side.lower()
    if lower_lake_side == "wait":
        house = input("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, "
                      "one blue. Which colour do you want to choose?\n")
        lower_house = house.lower()
        if lower_house == "blue":
            print("Congratulations, you won.")
        elif lower_house == "yellow":
            print("It's a room full of fire. Game Over.")
        elif lower_house == "red":
            print("A room of beasts, Game Over.")
        else:
            print("You an unexisting door. Game Over.")
    else:
        print("Game Over, the shark ate you up.")
else:
    print("Game Over, you fell into a hole.")


