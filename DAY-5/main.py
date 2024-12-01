# LOOPS
# fruits = ["Apple", "Pear", "Pawpaw"]
# for fruit in fruits:
#     print(fruit)


# A program to calculate the average student height
# student_heights = input("Enter a list of student heights.").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# num_of_students = 0
# for student in student_heights:
#     num_of_students += 1
# print(num_of_students)
#
# average_height = total_height / num_of_students
# print(f"Average height is {average_height}")




# highest score

# student_scores = input("Input list of student scores.").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         hieghest_score = score
# print(f"The highest score in the class is: {highest_score}")


total_number = 0
for number in range(1, 101):
    total_number = total_number + number
    print(total_number)


# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
#
# # OR
#
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#       total += number
# print(total)




# FIZZBUZZ
# #
# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         number = "FizzBuzz"
#     elif number % 3 == 0:
#         number = "Fizz"
#     elif number % 5 == 0:
#         number = "Buzz"
#     print(number)

#
#
# # OR
# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)