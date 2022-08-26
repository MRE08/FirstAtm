print("Thank you for choosing Miracle\'s ATM")
print('Welcome To Mirace\'s ATM!')
pin=int(input("Please enter your 4 digit password: "))
#Ammount = 25000
if(pin == 1234):
    print('Welcome, Kingsley Osifo')
    print("1-Withdraw")
    print("2-Balance Enquiry")
    transactions = int(input("Please choose transactions: "))
    if (transactions==1):
        Withdraw=int(input("Enter withdraw amount: "))
        if ((Withdraw>5000) and (Withdraw<50000)):
            print("Please take your amount:N", Withdraw)
            print('Would you like to make another transaction?')
            print('1.Yes','2.No')
            decision = int(input('Choice:'))
            if (decision==1):
                print()
        else:
            print('Insufficient Funds')

    elif(transactions==2):
        print("You have N50000")

else:
    print("Wrong pin number")
#Second Attempt
    pin2=int(input('This is your last trial:'))

    if(pin2 == 1234):
        print('Welcome, Kingsley Osifo')
        print("1-Withdraw")
        print("2-Balance Enquiry")
    transactions = int(input("Please choose transactions: "))
    if (transactions == 1):
        Withdraw=int(input("Enter withdraw amount: "))

        
        print("Please take your amount:", Withdraw)
        if ((Withdraw>5000) and (Withdraw<50000)):
            print("Please take your amount:N", Withdraw)
        else:
            print('Insufficient Funds')
    elif(transactions==2):
        print("You have N50000")
       

    else:
            print("Wrong choice")