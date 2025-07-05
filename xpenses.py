

def tracker():

    print("Choose an opton", end="\n")
    print("1.Add expense")
    print("2.View summary")
    print("3.Exit")
    choice=int(input("Enter choice(1/2/3)"))

    if choice == 1:

        add_expense()
    elif choice == 2:
        show_summary()
    elif choice == 3:
        print("Exiting tracker, stay smart")
    else:
        print("Invalid input")

#start tracker
tracker()