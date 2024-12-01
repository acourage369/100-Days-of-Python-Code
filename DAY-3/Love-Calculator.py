print("WELCOME TO THE LOVE CALCULATOR")
name1 = input("What is your name? ")
name2 = input("what is his/her name? ")

# counting of letters in combine_names corresponding to "TRUE".
combine_names = name1 + name2
lower_case_name = combine_names.lower()
countT = int(lower_case_name.count("t"))
countR = int(lower_case_name.count("r"))
countU = int(lower_case_name.count("u"))
countE = int(lower_case_name.count("e"))

sum_count_true = countU + countE + countR + countT

# counting of letters in combine_names corresponding to "LOVE".
countL = int(lower_case_name.count("l"))
countO = int(lower_case_name.count("o"))
countV = int(lower_case_name.count("v"))
countE = int(lower_case_name.count("e"))

sum_count_love = countL + countO + countV + countE


love_score = str(sum_count_true) + str(sum_count_love)
new_love_score = int(love_score)

if (new_love_score < 10) or (new_love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (new_love_score >= 40) and (new_love_score <= 50):
    print(f"Your score is {new_love_score}, you are alright together.")
else:
    print(f"Your score is {new_love_score}.")
