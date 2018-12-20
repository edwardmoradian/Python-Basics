    
# passing arguments to functions
# 1. we can have 0 or more parameters per function
# 2. parameters are local variables

def add(num1, num2):
    sum = num1 + num2
    print(sum)
    
def crazy_fun(i):
    while i > 0:
        print("hello")
        i -= 1
    
def main():
        add(8,6)    # 8 and 6 are arguments
                    # with this call: num1 = 8 and num2 = 6
        crazy_fun(5)
main()