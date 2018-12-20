#### Sentinel

Sentinel = -1   # sentinel value

# Initialize a variable to 0 to score the total
total = 0

# Ask the user for a number
n = int(input("Enter a number, -1 to quit:"))

# While that number isn't the sentinel
while n != Sentinel:
       # Add that number to my total
       total += n
       # Grab the next number
       n = int(input("Enter a number, -1 to quit:"))
       
# Show them their total
print(total)