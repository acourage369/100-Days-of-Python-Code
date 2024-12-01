# # Describe the bug
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the bug
# from random import randint
# dice_img = ["@", "#", "$", "%", "&", "?"]
# dice_num = randint(1, 6)
# print(dice_img[dice_num - 1])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#     print("You are millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fix the Erros
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}. ")

# # Print is your friend
# pages = 0
# word_paper_page = 0
# pages = int(input("Number of pages: "))
# word_paper_page = int(input("Number of words per page: "))
# total_words = pages * word_paper_page
# print(total_words)

# Use a debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1,2,3,5,8,13])


number = int(input("Which number do you want to check?  "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")