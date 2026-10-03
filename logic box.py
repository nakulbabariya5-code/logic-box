print("Welcome to the Pattern Generator and Number Analyzer!")

while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    # Option 1: Generate Pattern
    if choice == 1:

        rows = int(input("Enter the number of rows for the pattern: "))

        print("\nPattern:")

        for i in range(1, rows + 1):
            print("*" * i)

    # Option 2: Analyze Range
    elif choice == 2:

        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for number in range(start, end + 1):

            if number % 2 == 0:
                print(f"Number {number} is Even")
            else:
                print(f"Number {number} is Odd")

            total = total + number

        print(f"Sum of all numbers from {start} to {end} is: {total}")

    # Option 3: Exit
    elif choice == 3:

        print("Exiting the program. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
