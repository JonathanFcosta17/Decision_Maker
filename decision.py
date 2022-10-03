# This is a simple decision maker that can be used in the terminal if you don't want to use the discord bot.

from decision_class import DecisionMaker

# Geting the list os options and choosing one

print('''Welcome to the Decision Maker!
Enter a list of options separated by commas:
Example: 'Option 1, Option 2, Option 3'.''')

options = input("Enter your options: ")

# Create a decision maker object
decision = DecisionMaker(options)

# Asking if the user wants to add weights
print("\nWould you like to add some weight to the options?")
print("Enter 'y' for yes and 'n' for no")

# Looping until the user enters a valid answer
while True:
    answer = input("Enter your choice: ").lower()

    # If the user doesn't want to add weights
    if answer == 'n':
        print("\nYou asked The Great Decision Maker what to do.")
        print(
            f"The Great Decision Maker says: {decision.make_decision_simple()}")
        break

    # If the user wants to add weights
    elif answer == 'y':
        print(f"This is the list of options that you entered: {options}")
        weights = input("Enter the weights: ")
        print("\nYou asked The Great Decision Maker what to do.")
        print(
            f"The Great Decision Maker says: {decision.make_decision_weighted(weights)}")
        break

    else:
        print("Invalid input")
