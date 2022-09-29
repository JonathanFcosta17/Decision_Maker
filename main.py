from decision_class import DecisionMaker

# Geting the list os options and choosing one
print("Welcome to the Decision Maker")
print("Enter a list of options separated by commas")
print("Example: 'Option 1, Option 2, Option 3'")
options = input("Enter your options: ")

decision = DecisionMaker(options)  # Create a decision maker object

print("\nWould you like to add some weight to the options?")
print("Enter 'y' for yes and 'n' for no")
while True:
    answer = input("Enter your choice: ").lower()
    if answer == 'n':
        print("\nYou asked The Great Decision Maker what to do.")
        print("The Great Decision Maker says: " +
              decision.make_decision_simple())
        break
    elif answer == 'y':
        print(f"This is the list of options that you entered: {options}")
        weights = input("Enter the weights: ")
        print("\nYou asked The Great Decision Maker what to do.")
        print("The Great Decision Maker says: " +
              decision.make_decision_weighted(weights))
        break

    else:
        print("Invalid input")
