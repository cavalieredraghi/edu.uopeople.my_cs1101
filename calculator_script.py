# defining my functions before starting the base program


#I prefer integers to floats as they don't take up as much space as floats. Though I will use floats in this. 
def getFloat(prompt):
    while True:
        x= float(input(prompt))
        return x
def getOperator ():
    while True:
        operator= input("Which operator do you chose? +, -, /, *")
        if operator == "+" or operator == "-" or operator == "/" or operator == "*":
            return operator
        else:
            print("You have entered incorrectly try again.")

def doWork (oper, x, y):
    if op == "+":
        return x+y
    elif op == "-":
        return  x-y
    elif op == "*":
        return x*y
    elif x != 0 and y != 0 and op == "/":
        return x/y
    else:
        print("Either your first or last number was 0.  You can not divide.")

while True:
    print("This is a console calculator.")

    num1 = getFloat("First number: ")
    num2= getFloat("Second number: ")
    op = getOperator()
    end = doWork(op,num1,num2)

    print("Results: \n >>>", end)

    cont = input("Again? Y/N ")

    if cont != "Y":
        break

#Was my old code before critques.

#def multiply(x,y):
    #z=x*y
   #print(z)
    
#def subtract(x,y):
   # z=x-y
   # print(z)
    
#def divide(x,y):
   # z=x/y
   # print(z)
    
#def add(x,y):
    #z=x+y
   # print(z)

    #putting the program in a small loop to help with some error checking.
    #\n just creates a new line for the ease of seeing in the output file.

#while True:
#    operation = input("What would you like to do? *,/,+,- \n")

 #   if operation == "+":
  #      x=int(input("First number: \n"))
   #     y=int(input("Second number: \n"))
    #    add(x,y)
    #    break
 #   elif operation == "/":
  #      x=int(input("First number: \n"))
   #     y=int(input("Second number: \n"))
    #    divide(x,y)
     #   break
   # elif operation == "-":
    #    x=int(input("First number: \n"))
     #   y=int(input("Second number: \n"))
      #  subtract(x,y)
       # break
   # elif operation == "*":
    #    x=int(input("First number: \n"))
     #   y=int(input("Second number: \n"))
      #  multiply(x,y)
       # break

    #else:
     #   print("that was not a correct operation...")
        #loop will start again if one of the operators is not put in by user. 
        
