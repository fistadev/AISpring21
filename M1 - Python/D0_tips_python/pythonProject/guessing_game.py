secret_word = "llama"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses! Game over!!")
else:
    print("Congratulations!! You win!")





# secret_word = "llama"
# guess = ""
#
# while guess != secret_word: # infinite looping
#     guess = input("Enter guess: ")
#
# print("Congratulations!! You win!")