#creating the function to be called
def bool_test(a,b):
    #creating a if else statement for the possible different booleans.
    if a>b:
        print("1")
    elif a==b:
        print("0")
    elif a<b:
        print("-1")

#creating a loop for ease of redoing the process
n=1

while n==1:
    print("Testing boolean expressions, please input a number: ")
    #making local variables for the function to use.
    a=int(input())
    print("Please input a second number: ")
    b=int(input())

    bool_test(a,b)
