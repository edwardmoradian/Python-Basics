
# we can use the in operator to determine if an item exists in a list
# key: the in operator returns true or false

def main():
    nums = [8,6,7,5]
    number = 6
    
    # this asks the question: does number exist in list nums?
    if number in nums:
        print("Found it\n")
    else:
        print("Did not find it!\n")
    
    # Is it the case that number does not exist in nums?
    if number not in nums:
        print("Number is not in nums!\n")
    else:
        print("Number is in nums!\n")
    
main()