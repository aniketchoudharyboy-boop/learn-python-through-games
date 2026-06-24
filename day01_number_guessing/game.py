# secret_number = 25
# counter = 5
# print("Welcome to the Number Guessing Game!")


######## Simple statements and logic without function and loop##########
# user_guess_number = int(input("Guess the secret number between 1 and 100: ")) #int() function is used to convert the string input to integer

# concatenation through + operator
# print("You guessed:"+user_guess_number) 

# print("You guessed:") 
# print(user_guess_number)

#using str() function to convert the integer to string for concatenation
# print("You guessed:"+str(user_guess_number)) #str() function is used to convert the integer to string

#f-string is used for string formatting
# print(f"You guessed: {user_guess_number}. The counter starts from {counter} seconds.")

#Logic 1: either guessed number is correct or wrong
# if user_guess_number == secret_number:
#     print(f"Congratulations! You guessed the secret number {secret_number}.")
# else:
#     print(f"Sorry, that's not the secret number. The secret number was {secret_number}.")

#Logic 2: either the numer is gretaer or equal or less than the secret number
#1st method: using if only
# if user_guess_number < secret_number:
#     print("Your guess is too low.")
# if user_guess_number > secret_number:
#     print("Your guess is too high.")
# if user_guess_number == secret_number:
#     print("Your guess is correct!")

#2nd method: using if-else only
# if user_guess_number > secret_number:
#     print("Your guess is too high.")
# else:
#     if user_guess_number < secret_number:
#         print("Your guess is too low.")   
#     else:
#         print("Your guess is correct!")

#3rd method: using if-elif-else
# if user_guess_number > secret_number:
#     print("Your guess is too high.")
# elif user_guess_number < secret_number:
#     print("Your guess is too low.")
# else:
#     print("Your guess is correct!")

######## Simple statements and logic without function but using loop and counter(retries) to give retries until counter reach 0 ##########

# while counter > 0:
#     user_guess_number = int(input("Guess the secret number between 1 and 100: ")) #int() function is used to convert the string input to integer
#     if user_guess_number > secret_number:
#         print("Your guess is too high.")
#     elif user_guess_number < secret_number:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is correct!")
#         break
#     counter -= 1

# if counter == 0:
#     print("Thanks for playing the game. You have used all your attempts.")
# else: 
#     print(f"Congratulations! You guessed the secret number {secret_number}.")

########logic with function and using loop and counter(retries) to give retries until counter reach 0 ##########

# def number_guessing_game():
#     secret_number = 25
#     counter = 5
#     print("Welcome to the Number Guessing Game!")
#     while counter > 0:
#         user_guess_number = int(input("Guess the secret number between 1 and 100: ")) #int() function is used to convert the string input to integer
#         if user_guess_number > secret_number:
#             print("Your guess is too high.")
#         elif user_guess_number < secret_number:
#             print("Your guess is too low.")
#         else:
#             print("Your guess is correct!")
#             break
#         counter -= 1

#     if counter == 0:
#         print("Thanks for playing the game. You have used all your attempts.")
#     else:
#         print(f"Congratulations! You guessed the secret number {secret_number}.")

# if __name__ == "__main__":
#     number_guessing_game()

########logic with reusable and many functions and using loop and counter(retries) to give retries until counter reach 0 ##########

def data():
    secret_number = 25
    counter = 5
    return secret_number, counter

secret_number, counter = data()
print("Welcome to the Number Guessing Game!")
while counter > 0:




