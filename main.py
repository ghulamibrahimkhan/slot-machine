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

def main():
    balance = deposit()
