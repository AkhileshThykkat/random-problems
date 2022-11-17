## stone  paper scissor
import random as rd
li = ["stone","paper","scissor"]
def game(user, computer):
    if user == computer:
         computer_score = 'D'
         user_score = computer_score
         print(f"user score:{user_score} || computer score:{computer_score}")
    elif user  == "stone" and computer  == "paper":
        computer_score = 'W'
        user_score = 'L'
        print(f"user score:{user_score} || computer score:{computer_score}")

    elif user == "stone" and computer == "scissor":
        computer_score= 'L'
        user_score = 'W'
        print(f"user score:{user_score} || computer score:{computer_score}")

    elif user == "paper" and computer == "scissor":
        computer_score = 'W'
        user_score = 'L'
        print(f"user score:{user_score} || computer score:{computer_score}")

    elif user == "paper" and computer == "stone":
        computer_score = "L"
        user_score = 'W'
        print(f"user score:{user_score} || computer score:{computer_score}")

    elif user  == "scissor"  and computer == "stone":
        computer_score = "W"
        user_score = 'L'
        print(f"user score:{user_score} || computer score:{computer_score}")

    elif user == "scissor" and computer == "paper":
        computer_score = 'L'
        user_score = "W"
        print(f"user score:{user_score} || computer score:{computer_score}")

    else:
        print("enter a valid input ")


no = int(input("no of times you wanna play?:"))
for i in range(no):
    user_input = input("stone||paper||scissor:")
    computer_input = rd.choice(li)
    print(f"computer played:{computer_input}")
    game(user=user_input,computer=computer_input)





