print("Welcome to the Pattern generator and number analyzer!")
while True:
    print("\nSelect an option:")
    print("1. generate a Pattern")
    print("2. analyze a range of numbers")
    print("3. exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)
    elif choice == 2:
        start_num= int(input("\nEnter the start of the range: "))
        end_num = int(input("Enter the end of the range: "))
        total = 0
        for number in range(start_num, end_num + 1):
            if number % 2 == 0:
                print(f"Number {number} is Even")
            else:
                print(f"Number {number} is Odd")
            total += number
        print(f"Sum of all numbers from {start_num} to {end_num} is: {total}")
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

