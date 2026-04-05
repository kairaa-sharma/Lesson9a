num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
def checkequal(num1, num2):
    if ((num1 ^ num2) != 0):
        print("The numbers are inequal!") 
    else:
        print("The numbers are equal!")

checkequal(num1, num2)        