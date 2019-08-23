print ("Welcome to the BANK OF RACHEL.")

accountHolderName = input("What is your name?") #prompts user for name
pin = int(input("Create a 4-digit pin number:")) #prompts user for pin

# PROMPTS USER FOR BANK OPTIONS:
userInput = int(input((f' Please choose one of following options:\n'
                   f'1) Check balance \n'
                   f'2) Add money to account\n'
                   f'3) Withdraw money from account\n'
                   f'4) Quit\n'
                   f' > What will you like to do? \n')))
#declares values and sets them zero!

accountBalance = 0
deposit = 0
withdrawal = 0

#BANK MENU:
while userInput != 4:


    if userInput == 1: #prints current balance
        print("CHECK BALANCE")
        print (f'Your account balance is ${accountBalance}.')

    if userInput == 2: #allows user to ADD funds
        print ("DEPOSIT FUNDS")
        deposit =int(input(f'How much would {accountHolderName} like to deposit into this account?'))
        accountBalance = accountBalance + deposit
        print (f'Your account balance is now ${accountBalance}.')
## CHECKS FOR PIN BEFORE ALLOWING USER TO WITHDRAW FUNDS
    if userInput ==3:
        print("WITHDRAW FUNDS")
        pincheck = int(input("What is your 4-digit pin?")) #asks user to verify their pin
        while pincheck != pin: #checks to see if the pin entry matches
            print ("INCORRECT PIN. PLEASE TRY AGAIN.")
            pincheck = int(input("What is your 4-digit pin?"))
        else:
            withdrawal=int(input(f'How much would {accountHolderName} like to withdraw?'))
            if withdrawal > accountBalance: #IF THE AMOUNT THEY WANT TO TAKE
                # OUT IS MORE THAN THE BALANCE THEY CAN NOT REMOVE FUNDS
                print("INSUFFICIENT FUNDS.")
            else: #if the account users balance supports the withdrawal then subtract and print the new balance
                accountBalance = accountBalance - withdrawal
                print (f'Your account balance is now ${accountBalance}.')


    #RETURNS USER TO BANK MENU.
    userInput = int(input((f' Please choose one of following options:\n'
                       f'1) Check balance \n'
                       f'2) Add money to account\n'
                       f'3) Withdraw money from account\n'
                       f'4) Quit\n'
                       f' > What will {accountHolderName} like to do? \n')))

#end of loop (and it works :)))))))