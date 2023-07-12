''' Calculator 
'''


num1 = float(input("Enter the number1: "))
num2= float(input("Enter the number2: "))
oper = input("Enter the operation: ")

if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    print(round((num1/num2),2))    
