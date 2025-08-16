import random as rd

def numguess():
    number = rd.randint(1, 100)
    print('Welcome to number guessing game!!','I have chosen a number between 1 and 100', 'You have limited attempts to guess it correctly',sep='\n')
    print('Select a hardness level', '0 - Easy (10 Attempts)', '1 - Medium (5 Attempts)', '2 - Hard (3 Attempts)',sep='\n')
    hardness = int(input())
    lvl = (0,1,2)
    while hardness not in lvl:
        hardness = int(input('Invalid input, acceptable inputs are 0, 1 or 2 only: '))
    if hardness == 0:
        attempts = 10
    elif hardness == 1:
        attempts = 5
    elif hardness == 2:
        attempts = 3
    attempt = attempts - 1
    #print(number) #for debugging purpose only
    x = 0
    while x < attempts:
        guess = int(input('Enter your guess: '))
        if guess > 100 or guess < 1:
            print(f'Sorry, guess a number between 1 and 100, You have',attempt - x,'attempts left')
        elif guess == number:
            print(f'Congratulations! You guessed the number correctly! in',x+1,'attempt(s)')
            break
        elif guess > number:
            print(f'Sorry, guess a lower number, You have',attempt - x,'attempts left.')
        elif guess < number:
            print(f'Sorry, guess a higher number, You have', attempt - x, 'attempts left.')
        x += 1
    print('Thank you for playing!, Do you want to play again? 0-Yes 1-No')
    choice = int(input())
    if choice == 1:
        print('Thank you for playing!')
        exit()
    elif choice == 0:
        numguess()
    else:
        print("To avoid coding, I'll take that as a NO, Thank you for playing! :P ")
        exit()
numguess()