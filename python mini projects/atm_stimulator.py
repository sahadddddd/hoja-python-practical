# Menu

# ====ATM====
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Features


# . Initial Balance = ₹5000
# . Deposit money
# . Withdraw money
# . Cannot withdraw more than balance
# · Keep running until Exit

#  Functions to Create
# show_menu()
# deposit()
# withdraw()
# check_balance()

balance=5000

def show_menu():
    print("\n====ATM====")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

def check_balance():
    print(f"your current balnce is ₹{balance}")

def deposit():
    global balance
    amount=int(input("enter the amount:₹"))
    balance += amount
    print(f"₹{amount} deposited successfully. ")


def withdraw():
     global balance
     amount=int(input("enter the amount:₹"))
     if amount<=balance:
         balance -= amount
         print(f"₹{amount} withdrawn succesfully")
     else:
         print("Insufficient balance! Withdrawal denied")




while True:
    show_menu()
    choice=input("enter your choice (1-4):")

    if choice=="1":
        check_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice =="4":
        print("thankyou for using ATM goodbye!")
        break
    else:
        print("invalid choice try again")
