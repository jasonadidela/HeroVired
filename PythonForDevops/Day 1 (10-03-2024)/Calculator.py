print("welcom to my Calculator")

x = int(input("Enter the first value: "))

y = int(input("Enter the second value; "))

def sum(num1,num2):
    
    result = num1 + num2    

    print("the addition of ",num1,"and",num2,"is",result)

def sub(num1,num2):
    
    result = num1 - num2    

    print("the Subtration of ",num1,"and",num2,"is",result)

def mul(num1,num2):
    
    result = num1 * num2    

    print("the Multiplication of ",num1,"and",num2,"is",result)

def div(num1,num2):
    
    result = num1 / num2    

    print("the division of ",num1,"and",num2,"is",result)

print("Please Enter the any Key to perform Arithamatic Operation:")

print("For addition Press: 1")

print("For Subtration Press: 2")

print("For Division Press: 3")

print("For Multiplication Press: 4")

key = int(input("Enter the Key: "))

if key == 1: sum(x,y)

elif key == 2: sub( x, y)

elif key == 3: div( x, y)

elif key == 4: mul( x, y)

else: print("invalid key, Please Enter Valid key")