import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_sloth_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        colum = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            colum.append(value)
        columns.append(colum)
    return columns

def print_slot_columns(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("What would you like to deposit? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount nust be greter than 0$.")
        else:
            print("PLease enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter a number of lines to bet on. (1-{MAX_LINES}) ? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                 break
            else:
                 print("Enter valid numbers of line")
        else:
             print("PLease enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET and amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}$ - {MAX_BET}$.")
        else:
            print("PLease enter a number.")
    return amount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet =  get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough to bet. Your current balance is: {balance}$")
        else:
            break
    slots = get_sloth_machine_spin(ROWS,COLS,symbols)
    print_slot_columns(slots)

main()
