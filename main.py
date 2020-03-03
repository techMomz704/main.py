# ask the user to input their experience by asking them a question using the input() function
# Use an if/elif/else statement to check if the user chose option 1, 2, 3, or 4
# if the user chose option 1, print out 'Expect between $40,00 and $60,000 for your level of experience'
# else if the user chose option 2, print out 'Expect between $60,000 and $80,000 for your level of experience'
# else if the user chose option 3, print out 'Expect between $80,000 and $120000 for your level of experience'
# else if the user chose option 4, print out 'Expect at least $130,000 for your level of experience'
# homework 1 - enter a default message if the user does not enter a valid option - else:print(10*"*" + "Invalid Entry! Please enter 1, 2, 3 or 4" + 10 * "*")
# TODO



users_experience = input("How many years experience do you have developing software?\n [1] Less than 1 year"
                         " \n [2] 1 - 3 years of experience  \n [3] 3 - 8 years of experience \n [4] "
                         "8+ years of experience \n")

users_experience = int(users_experience)

users_coding_languages = input("What languages do you know? (separate each language by a comma)")
print("Before Split(): " + users_coding_languages)

users_coding_languages = users_coding_languages.split(",")
print("After Split(): " + str(users_coding_languages))


if users_experience == 1:
    print("Expect between $40,000 and $60,000 for your level of experience")
    if len(users_coding_languages) < 3:
        print("learn some more languages: deduct 10K from the expected salary.")

elif users_experience == 2:
    print("Expect between $60,000 and $80,00 for your level of experience")
    if len(users_coding_languages) < 3:
        print("learn some more languages: deduct 5K from the expected salary.")
    if len(users_coding_languages) > 5:
            print("You're in good shape! Don't be afraid to ask for more than the Expected Salary.")

elif users_experience == 3:
    print("Expect between $80,000 and $120000 for your level of experience")

elif users_experience == 4:
    print("Expect at least $130,000 for your level of experience")

else:
    print(10*"*" + "Invalid Entry! Please enter 1, 2, 3 or 4" + 10 * "*")