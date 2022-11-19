MIN = 0
MAX = 100
def get_guess():
    from random import choice
    li = list(range(MIN,MAX+1))
    guess = choice(li)
    return guess
def get_input():
    while True:
        a = input("enter the guess:")
        if a.isdigit():
            number = int(a)
            if MIN<=number<=MAX:
                break
            else:
                print(f"the number should be between {MIN} and {MAX}")
        else:
            print("please enter a valid input")
    return number
def check(guess,number):
    if number==guess:
        return True
    else:
        return False
def main(guess):
    number = get_input()
    validation = check(guess=guess,number=number)
    print(f"number={number}\nguess={guess}")
    if validation:
        print(f"you guessed it right")
    if not validation:
        main(guess)
guess = get_guess()
main(guess)
