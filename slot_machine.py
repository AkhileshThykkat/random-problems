import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET =100
ROWS = 3
COLS = 3
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                # winning_line.append(0)
                break
        else:
            winnings +=values[symbol] * bet
            winning_line.append(line + 1)
    return winnings,winning_line


def print_slotmachine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns) - 1:
                print(column[row],end = ' | ')
            else:
                print(column[row],end='')
        print()

def get_slotmachine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("enter the amount you want to deposit : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount should be greater than zero")
        else:
            print("amount should be a digit")

    return amount
def no_of_lines():
    while True:
        lines = input("enter the number of lines to bet on"+f" (1~{MAX_LINES}) : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("number must be from 1~3 only")
        else:
            print("input must be a digit")
    return lines
def get_bet():
    while True:
        amount = input("enter the amount you want to bet on each line : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print("amount should be in between" + f" ${MIN_BET} - {MAX_BET}")
        else:
            print("amount should be a digit")

    return amount
def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press any key to play |(q to quit)|")
        if answer.upper() =='Q':
            break
        balance += spin(balance=balance)
    print(f"you are left with ${balance}")

def spin(balance):
    lines = no_of_lines()
    while True:
        bet  = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you dont have enough balance to raise the bet\nbalance is {balance}")

            print("raise your deposit || or quit the game",end="\n")
            k = input("enter y for depositing n for quitting")
            if k.upper() == 'Y':
                balance = deposit()
            else:
                exit()
        elif total_bet<=balance:
            break

    print(f"total bet is = {total_bet}\nnumber of lines is = {lines}")
    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings,winning_line= check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    if len(winning_line) != 0:
        print(f"you won on",*winning_line)
    else:
        print("you won on zero lines")  
    return winnings - total_bet
main()
