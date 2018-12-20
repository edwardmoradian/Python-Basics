a = 3.14159
b = 2.17
c = 6.66
d = 42.4242

# print(a,b,c,d)

# print(a,b)
# print(c,d)

# We'll use format() to change format
# print(format(a,".1f"),format(b,".1f"))  # f for floating point number, 1 means only 1 decimal point
# print(format(c,".1f"),format(d,".1f"))

### x.yz
# w = justification: < ^ >
# x = field width
# y = number of decimal places
# z = what type of data should be formatted as
print(format(a,"10.1f"),format(b,"10.1f"))  # f for floating point number, 1 means only 1 decimal point
print(format(c,"10.1f"),format(d,"10.1f"))  # 10 is the scale and 1 is the precision

print(format(a,"<10.1f"),format(b,">10.1f"))  # < is for justification on the left
print(format(c,"^10.1f"),format(d,"10.1f"))  # ^ is for justification on the center

t = format(a,".3e")     # e for scientific notation
print(t)

print(format(.50,".0%")) # .0 to show no decimal places

print(format("hello","10s"), format("world","10s"))

print(format(1000000000,",d"))  # , for commas in a number, d is for integer














