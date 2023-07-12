''' This is the solution of problem 2 of the practice set'''

print("Get table of any number you enter")
num= int(input("Enter the number: "))
for i in range (1 , 11):
    print (num, '*', i , '=' , num*i)