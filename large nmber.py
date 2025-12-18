def get_valid_number(prompt):
    """
    Function to get a valid number from user with error handling
    Keeps asking until a valid number is entered
    """
    while True:
        try:
            # Try to convert user input to a number
            number = float(input(prompt))
            return number
        except ValueError:
            # If user enters something that's not a number, show error
            print("Invalid input! Please enter a valid number.")

def find_largest(numbers):
    """
    Function to find the largest number in a list
    Returns both the largest number and its position
    """
    largest = numbers[0]
    position = 1
    
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            position = i + 1
    
    return largest, position

# Main program starts here
print("=" * 50)
print("     LARGEST NUMBER FINDER")
print("=" * 50)

# Ask user how many numbers they want to compare
while True:
    try:
        count = int(input("\nHow many numbers do you want to compare? (minimum 2): "))
        if count >= 2:
            break
        else:
            print("Please enter at least 2 numbers to compare.")
    except ValueError:
        print("Please enter a valid number.")

# Collect all numbers from user
numbers = []
for i in range(count):
    number = get_valid_number(f"Enter number {i + 1}: ")
    numbers.append(number)

# Find the largest number
largest, position = find_largest(numbers)

# Display results
print("\n" + "=" * 50)
print("RESULTS:")
print("=" * 50)
print(f"Numbers entered: {numbers}")
print(f"The largest number is: {largest}")
print(f"It was the number #{position} that you entered")
print("=" * 50)

# Ask if user wants to try again
while True:
    choice = input("\nDo you want to find another largest number? (y/n): ").lower()
    if choice == 'y':
        print("\n")
        # Restart the program logic
        while True:
            try:
                count = int(input("How many numbers do you want to compare? (minimum 2): "))
                if count >= 2:
                    break
                else:
                    print("Please enter at least 2 numbers to compare.")
            except ValueError:
                print("Please enter a valid number.")
        
        numbers = []
        for i in range(count):
            number = get_valid_number(f"Enter number {i + 1}: ")
            numbers.append(number)
        
        largest, position = find_largest(numbers)
        
        print("\n" + "=" * 50)
        print("RESULTS:")
        print("=" * 50)
        print(f"Numbers entered: {numbers}")
        print(f"The largest number is: {largest}")
        print(f"It was the number #{position} that you entered")
        print("=" * 50)
    elif choice == 'n':
        print("\nThank you for using Largest Number Finder! Goodbye")
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")
