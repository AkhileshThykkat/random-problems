from random import randint
number = randint(0,100)
count = 0
print(number)
i = int(input("number of times you want to play:"))
total = i

while i != 0:
    try:guess = int(input("guess:"))
    except ValueError:
        print("numbers are only permitted")
        break
    # noinspection PyUnboundLocalVariable
    if 0 <= guess <= 100:
        if guess != number:
            print("try again")
            flag = False
            count = count + 1
        elif guess == number:
            print(f"congratulations you guessed it right")
            flag = True
            break
    else:
        print(f"value must be between {0} and{100}")
    i = i - 1
# noinspection PyUnboundLocalVariable
if not flag:
    score = 0
else:
    score = 100-(((count + 1) / total) * 100)
print(f"the correct number is {number}")
print(f"your score is {round(score)}")
