import random

# Display a welcome message to the user
print("WELLCOME TO THE NUMBER GUSSING GAME. Please Enter your choice of number in which you would like to guess the number. GOOD LUCK!!!")

# Get the range boundaries for the guessing game from the user
starting_number = int(input("Enter the First number : "))
second_number = int(input("Enter the Second number : "))

# Generate a random integer between (and including) the two numbers provided
Actual_number = random.randint(starting_number, second_number)

# Get the total number of attempts the user wants
attempt = int(input("Enter the number of attempt you would like to Guess a correct number : "))

# Display the rules and game parameters to the player
print(f"\nThe number is going to be between {starting_number} to {second_number}")
print(f"You have {attempt} CHANCE to WIN the GAME\n")

# Flag to track if the user successfully guessed the number
guessed_correctly = False

# Loop through the allowed number of attempts (from 1 to 'attempt')
for i in range(1, attempt + 1):
    # Prompt the user for their current guess
    guessed_number = int(input(f"Enter your {i} GUESS : "))
    
    # Check if the user's guess matches the randomly generated number
    if guessed_number == Actual_number:
        print("Congrats the guessed number is correct!")
        guessed_correctly = True
        break  # Exit the loop early since the user won
    else:
        # Inform the user they were wrong and provide a hint
        print("YOUR GUESS IS WRONG PLEASE TRY AGAIN ")
        
        if guessed_number > Actual_number:
            print("GUESS lower")
        else:
            print("GUESS higher")
        print("-" * 30)  # Visual separator between turns

# If the loop finishes and the user never guessed correctly, trigger Game Over
if not guessed_correctly:
    print(f"\nSORRY TRY AGAIN!!! THE GAME IS OVER you are out of attempts.")
    print(f"The correct Number was {Actual_number}")
