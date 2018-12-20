

#### import the math module, which contains prewritten functions for doing "math stuff"
import math # gives us access to math module functions

def main ():
    num =float(input("Give me: "))
    num = math.sqrt(num)
    
    print("The square root of your number is ", num)
    
    num = float(input("Give me: "))
    num = math.sin(num)
    print("The sin of your nummber is ", num, " radians")
    
main()