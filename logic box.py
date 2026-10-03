print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print()
    print("Menu:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("How many rows? "))
        print()
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == "2":
        start = int(input("Start number: "))
        end = int(input("End number: "))

        total = 0
        for number in range(start, end + 1):
            if number % 2 == 0:
                print(number, "is even")
            else:
                print(number, "is odd")
            total = total + number

        print("Sum from", start, "to", end, "is", total)

    elif choice == "3":
        print(" Good Bye! ")
        break

    else:
        print("Invalid choice, try again.") 
