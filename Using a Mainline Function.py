#### Add two numbers program

def get_num(s):     # s is the parameter
    print("Enter the", s,"number: ", end="")
    n = float(input())
    return n

def add_nums(a,b):
    c = a + b
    return c

def display(a):
    print("Your sum is:",a)

def main():
     go_again = "Y"
     while go_again == "Y":
         num1 = get_num("first") 
         num2 = get_num("second") 
         sum = add_nums(num1,num2)
         display(sum)
         go_again = input("Go Again?")
       
main()