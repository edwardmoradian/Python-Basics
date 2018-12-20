
# 2-dimensional list examples

ROWS = 3
COLS = 3

def main():
    nums = [[8,6,7],[5,3,0],[9,8,2]]    
    print(nums)
    
    for n in nums:
        print(n)
    
    nums[0][1] = 66
    print(nums)

    # for processing, you often need 2 loops
    total = 0
    
    for r in range(ROWS):
        for c in range(COLS):
            total += nums[r][c]
    
    print("your total is", total)
    
main()