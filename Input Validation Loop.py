#### Input Validation Loop

LegalAge = 21

# Ask the user for input
age = float(input("Enter your age: "))

# While the input is unacceptable
while age < LegalAge:
        # Tell them it's bad
        print("You are too young. Try again.")
        
        # Ask the user for input
        age = float(input("Enter your age: "))

print("Take a shot of Schnapps!")