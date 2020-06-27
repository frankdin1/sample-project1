keep_going = True
while keep_going:
    entry = False# this establishes a boolean for entry
    while not entry:# this runs the loop repeatedly as long as entry is false
        op = input("Select your operation" + "\n" "m = multiply" + "\n" +
               "d = divide" + "\n" + "a = add" + "\n" + "s = subtract" + "\n")# user input
        if op != "m" and op!= "a" and op!= "d" and op!= "s":
            print("Invalid Entry")# this keeps the boolean for entry false if the user enters none of the 4 operators
        else:
            entry = True# if the user eenters one of the 4 opertors, it breaks the while loop and moves on to the next part of the code

    num1 = float(input("Select your 1st number: "))#this converts the user input to float
    num2 = float(input("Select you 2nd number: "))

#each of the lines below perform the operation corresponding to the user input
    if op == "m":
        print(num1*num2)
    elif op == "d":
        print(num1/num2)
    elif op == "a":
        print(num1 + num2)
    else:
        print(num1 - num2)

    user2 = input("Do you want to do another operation? (y/n): ")
    if user2 == "y":
        keep_going = True
    else:
        keep_going = False
