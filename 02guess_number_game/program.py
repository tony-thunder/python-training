import random

print('------------------------------')
print('      GUESS THAT NUMBER GAME')
print('------------------------------')
print()

number = random.randint(0, 200)
guess = -1

while guess != number:
    guess_text = input('Guess a number between 0 and 200:')
    guess = int(guess_text)

    if guess < number:
        print('Too low.')
    elif guess > number:
        print('Too high.')
    else:
        print('You win.')