import sys
a = "not"
b = "that"

def message():
    # sys.argv takes the input from the terminal and adds it to a list 
    # index 0 in the sys.argv list is the name of the file
    # index 1-n is input from the terminal 
    if sys.argv[1] == "mads":
        print("hello and welcome")
        print(sys.argv[0])
    elif sys.argv[1] == "oliver":
        print(sys.argv[1], "you're not allowed")    
    else:
        # another way to print. istead of the way from java that uses + "something + "somethingelse"
        print(f"Not allowed {a} {b}")
        # used to choose a positon in the string 
        print(a[-1])
        print(b[0:3])

message()