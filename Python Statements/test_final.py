from random import randint
random_number = randint(1,100)

print(random_number)


guesses = [0]



while True:

    user_input = int(input("Enter the secretnumber : "))
    
    
    if user_input < 1 or user_input > 100:
        print("Out of Bounds")
        continue

    if user_input ==random_number:
        print(f"you won and the no of guesses you have taken is {guesses}")
        break

    guesses.append(user_input)

    

    if guesses[-2]:
        
        if abs(random_number-user_input) < abs(random_number - guesses[-2]):
            print("Warmer")
            print(guesses[-2])
            
        else:
            print("Colder")
        
        
            
    else:
        if abs(random_number-user_input) <=10:
            print("WARM")
        else:
            print("COLD")
        
    
   

    if user_input > random_number:
        print("Try a smaller number")
    elif user_input < random_number:
        print("Try a bigger number")

'''import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


guesses = [0]
print(num)


while True:

   # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    print(guesses)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
            print(guesses[-2])
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')'''


        
        


     
