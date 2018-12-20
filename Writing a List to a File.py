
# Lists and Files

# Writing a list to a file

def main():
    n = ["2","4","6","8"]
    
    # Method 1: Write out everything in the list to the file
    # This puts everything on one line and no spcaes if your list doesn't have spaces or new lines
    f = open("out.txt","w")
    f.writelines(n)
    
    f.close
    
    # Method 2: This can let me write stuff to separate lines
    f = open("out.txt","a")
    f.write("\n")
    for t in n:
        f.write(t + "\n")
    
    f.close
    
    # Writelines requires everything in the list to be a string, so what if you start off with a list of integers?
    temp_nums = []
    nums = [3,5,7,9]
    for i in nums:
        temp_nums.append(str(i))
    
    f = open("out.txt","a")
    f.writelines(temp_nums)
    
    f.close()
        
    # one other way of converting nums to strings:
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    
main() 
























