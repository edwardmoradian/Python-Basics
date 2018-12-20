
"""
Write a program that asks the user for 3 numbers and displays the average to 2 decimal places of precision
"""

print("Give me 3 numbers, I'll give you the average")

print("Give me the first number.")
num1 = input(":")
num1 = float(num1)

print("Give me the second number.")
num2 = input(":")
num2 = float(num2)

print("Give me the third number.")
num3 = input(":")
num3 = float(num3)


average = (num1 + num2 + num3)/3

print("Your average is ", format(average,".2f"), ".", sep="")