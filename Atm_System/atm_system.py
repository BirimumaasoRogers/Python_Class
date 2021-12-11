# Develop a system with one function that prompts a user to enter name, pin and once a pin is valid.
# When pin is correct ask user to enter an amount to withdraw and system should be able to determine if the user has sufficient
# Balance then the system should be able to reduce the balance on the account.
# Account balance should b displayed after withdraw.

name = 'Birimumaaso Rogers'
print("--------Welcome", name, "to the DFCU Bank Portal-------")
# trials = 3
# user_pin = 4567

def atm_system():
    trials = 3
    user_pin = 4567
    userDeposit = 500000
    pin = int(input('Please enter your Pin: '))
    if pin != user_pin:
        trials -= 1
        print("Wrong Pin, you have", trials, "trials left")
    else:
        userChoice = input('W: Withdraw => ')
        if userChoice == 'W':
            print("Your Account Balance is:",userDeposit)
            userWithdraw = int(input("Enter amount of money you want to withdraw: "))
            balance = userDeposit - userWithdraw
            print("Shs",userWithdraw,"has been withdrawn from your account")
    userExit = input("Would you like to continue? Y/N: ")
    if userExit == "N":
        print("Your Account balance is ",balance)
        print("--------Thank You For Using DFCU Bank--------")
    else:
        print("Please wait for further prompts")
        atm_system()
atm_system()
        


  
    

