import random
# class Error(Exception):
#     pass
player1 = 3
hint = input("Would you like to play with a hint? (yes or no): ")

number = random.randint(1, 10)

if hint.lower() == 'yes':
    if number <5:
        print("The number is less than 5.")
    else:
        print("The number is 5 or greater.")

#pull request test

while True:
    player_1_hp = input("Would you like to see your remaining attempts? (yes or no): ")
    if player_1_hp.lower() == 'yes':
        print(f"You have {player1} attempts remaining.")    

    guess = int(input("Please guess a random number between 1 and 10: "))

    if player1 == 0:
        print(f"You've run out of attempts. The correct number was {number}.")
        question = input("Would you like another try? (yes or no): ")
        if question.lower() == 'yes':
            task = input("What is 2+2? ")
            if task == '4':
                player1 +=2
                number = random.randint(1, 10)
                continue
            else:
                print("Incorrect answer. Exiting the game.")
                break
        break

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, that's not correct.")
        player1 -= 1
        
        
        hint = input("Would you like another hint? (yes or no): ")
        if hint.lower() == 'yes':
            if guess < number:
                print("The correct number is higher than your guess.")
            else:
                print("The correct number is lower than your guess.")
        continue


    