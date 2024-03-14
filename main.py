import random

# Computer make an random number and it's my job to guess it.
#def guess(limit):
#    random_number = random.randint(1, limit)
#    guess = 0
#    while guess is not random_number:
#        guess = int(input(f"Guess a number between 1 and {limit}: "))#
#
#        if(random_number < guess):
#            print("Your guess is too high!")
#        elif(random_number > guess):
#            print("Your guess is too low!")
#            
#    print(f"You made it! {guess} was a lucky number. Congrats!")

#guess(int(input("Welcome to guessing game! Please, set a limit: ")))

# I make an random numer and its computer job to guess it.
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        print(f"My guess is {guess}. ", end="")
        feedback = input(f"It's {guess} too high (H), too low (L), or correct (C)? ").upper()

        if(feedback == 'H'):
            high = guess-1
        elif(feedback == 'L'):
            low = guess+1

    print("Yeah, I made it!")
    

computer_guess(int(input("Welcome to guessing game! Please, set a limit: ")))
