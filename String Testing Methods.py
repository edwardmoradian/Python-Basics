## Here are some testing methods:
## isupper(), islower(), isdigit(), isalpha(), isalnum(), isspace()
## whitepace -> hidden backspace, tab
    
    if s.isdigit():
        print("It is all digits!")
    else:
        print("There are non digits in there. Nonnumbers that is")
        
    if s.islower():
        print("Everything is lower case!")
    else:
        print("Everything is not lower case")
    
    if "1234".isdigit():
        print("Yes")