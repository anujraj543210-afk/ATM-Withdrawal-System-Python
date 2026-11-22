# ATM-Withdrawal-System-Python
ATM Withdrawal System using Python Project Description  This is a simple ATM Withdrawal System developed using Python.  It allows users to withdraw money from their account and check their remaining balance.  Features Initial balance of ₹10,000 Withdraw money from the account 
balance=10000
withdrawal=True
while withdrawal:
    amount = int(input("enter your amount wihtdraw:"))
    if amount<=balance:
        print("amount debited")
        balance= balance-amount
        print("your current balanced",balance)
    else:
        print("insufficient balance")
        choice = input("do you need to withdraw again")
        if choice . lower()=="n":
            withdrawal=True
