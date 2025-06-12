##if statements

'''
Syntax  

if condition
   logic
elif condition:
   logic
else:
   logic
   
'''

## A program that accepts a mark from the user
# it grades the mark entered

print("Welcome to the GRADING SYSTEM!")
mark = int(input("please enter a mark"))
if mark <70: 
   print("Retake")
elif mark >100:
   print("Invalid mark,please re-enter") 
elif mark >89<100:
   print("you have A+")
elif mark >79<90:
   print("you have A")
elif mark >69<80:
   print("you have B")


else:
   print("Error")    
   


