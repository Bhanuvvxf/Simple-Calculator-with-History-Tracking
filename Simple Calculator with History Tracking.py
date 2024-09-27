#Simple Calculator with History Tracking

History = []

print("Welcome to the Simple Calculator!")

def Add():
    try:
        fs = int(input("Enter first number: ")) #fs is the frist number 
        ss = int(input("Enter second number: ")) #ss is the second number 
        r = fs + ss #r is the result 
        data = str(fs) + " + " + str(ss) + " = " + str(r)
        History.append(data)
    except ValueError:
        print("Enter only numbers . ")
    return r

def Substraction():
    try:
        fs = int(input("Enter first number: ")) #fs is the frist number 
        ss = int(input("Enter second number: ")) #ss is the second number 
        r = fs - ss #r is the result 
        data = str(fs) + " - " + str(ss) + " = " + str(r)
        History.append(data)
    except ValueError:
        print("Enter only numbers . ")
    return r

def Multiply():
    try:
        fs = int(input("Enter first number: ")) #fs is the frist number 
        ss = int(input("Enter second number: ")) #ss is the second number 
        
        r = fs * ss #r is the result 
        data = str(fs) + " * " + str(ss) + " = " + str(r)
        History.append(data)
    except ValueError:
        print("Enter only numbers . ")
    return r

def divide():
    try:
        fs = int(input("Enter first number: ")) #fs is the frist number 
        ss = int(input("Enter second number: ")) #ss is the second number 
        if ss == 0 :
            print("Division by zero is not allowed.")
            return "undefined"
        r = fs / ss #r is the result 
        data = str(fs) + " / " + str(ss) + " = " + str(r)
        History.append(data)
    except ValueError:
        print("Enter only numbers . ")
    return r

while True:
    print("Choose an operation:")
    print()
    print("1. Add","2. Subtract","3. Multiply","4. Divide","5. Show History","6. Clear History","7. Exit",sep="\n")
    print()

    try:
        c = int(input("Enter choice: ")) #c is the user choice 
    
    except ValueError:
        print("Enter only choice in number (not characters or symbals )")
        break
    
    if c == 1 :
            
            s = Add() # s is the solution and calling addition funtion
            print(f"Result: {s}")
            print("_"*20)
    
    elif c == 2 :

        s = Substraction()
        print(f"Result: {s}")
        print("_"*20)
    
    elif c == 3 :
        s = Multiply()
        print(f"Result: {s}")
        print("_"*20)
    
    elif c == 4 :
        s = divide()
        print(f"Result: {s}")
        print("_"*20)
    
    elif c == 5 :
            if len(History) == 0 :
                print("Sorry ! there are no operations . ")
        
            for j in History:
                print(History.index(j)+1,".",j)
            
            print("_"*20)
        
    
    elif c == 6 :
        History.clear()
        print("_"*20)
    
    elif c == 7 :
        print("Exiting the calculator. Thank you for using!")
        break

    else:
        print("Enter valid choice ! ")
        print("_"*20)

    
        

        
            



