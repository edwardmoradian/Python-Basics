
## Search and replace methods: endswith, find, replace, startswith

def main():
    s = "How now brown cow?"
    
    if s.endswith("cow?"):
        print("It does!")
    else:
        print("It does not!")

    if s.startswith("cow?"):
        print("It does!")
    else:
        print("It does not!")

    i = s.find("now")
    if i != -1:     # Does it exist and where
        print("I found it at", i)
    else:
        print("Not found!")

    t = s.replace("brown","orange")
    print(s,t)

# split() splits up a string into a list of strings
    
    a_list = s.split()
    print(a_list)
    
    s = "8,6,7,5"
    a_list = s.split(",")
    print(a_list)

main()






















