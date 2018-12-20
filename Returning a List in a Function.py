
# Return lists into functions

# Write a function that asks the user for 3 numbers, puts them in a list and returns the list

def spam():
    nums = []
    
    for n in range(1,4):
        print("Enter Number ", n, ": ",end="",sep="")
        a_num = float(input())
        nums.append(a_num)
    
    return nums

def main():
    a_list = spam()
    print(a_list)

main()