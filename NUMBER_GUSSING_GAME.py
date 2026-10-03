import random

print("WELLCOME TO THE NUMBER GUSSING GAME. Please Enter your choice of number in which you would like to guess the number. GOOD LUCK!!!")
starting_number = int(input("Enter the First number : "))
second_number = int(input("Enter the Second number : "))
Actual_number= random.randint(starting_number,second_number)
attempt = int(input("Enter the number of attempt you would like to Guess a correct number : "))
print(f"The number is going to be between {starting_number} to {second_number}")
print(f"You have {attempt} CHANCE to WIN the GAME")
for i in range(1,attempt+1,1):
    guessed_number= int(input(f"Enter your {i} GUESS : "))
    
    if guessed_number == Actual_number:
        print("Congrats the gussed number is correct")
        break 
    else:
        i = i+1
        print("YOUR GUESS IS WRONG PLEASE TRY AGAIN ")
        if guessed_number > Actual_number:
            print(" GUESS lower")
        else:
            print("GUESS higher")
if i==attempt+1:
    print(f"SORRY TRY AGAIN!!! THE GAME IS OVER you are out off attempt, The correct Number was {Actual_number} ")