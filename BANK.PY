#Bank
balance = 50
while True :
    print("========MENU========")
    print("Enter 'D' for Deposit ")
    print("Enter 'W' for Withdraw money")
    print("Enter 'C' for Check balance")
    print("Enter 'E' for Exit")
    user = input("Enter your choice:")

    if user == 'E' :
        print ("EXIT")
        break
    elif user == 'D' :
        deposit = float (input("Enter Your Deposit Amount:"))
        balance = deposit + balance
        print ("deposited successfully of Amount :", deposit)

        print("ooh! no cash back better luck next time !!")
    elif user == 'W' :
        withdraw = float(input ("Enter Your withdraw amount "))
        if withdraw > balance:
             print("---------------------->insufficient balance")

             print ("Check balance and deposit now and claim cashback upto 50")
        else :
             balance = balance - withdraw
             print ("withdrawal successfully of amount:", withdraw)

    elif user == 'C' :
        print ("-------------------->Balance :", balance)
    else:
        print("--------------------->invalid")
        