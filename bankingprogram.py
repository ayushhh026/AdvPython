# pythom banking program


def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount=int(input("Enter an amount to be deposited : "))
    if amount < 0:
        print("That is not a valuid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = int(input("Enter amount to be withdrawn : "))
    if amount >balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("-------------------------------")
        print("Banking Program")
        print("-------------------------------")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice = int(input("Enter your choice (1-4): "))
        print("-------------------------------")


        if choice == 1:
            show_balance(balance)
        elif choice ==2:
            balance+= deposit()
        elif choice ==3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running=False
        else:
            print("----------------Invalid choice ---------------")

    print("Thank you for banking with us")


if __name__ == '__main__':
    main()