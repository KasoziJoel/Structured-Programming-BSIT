



def is_prime():
    
    if n % 2 == 1:
        return True
        
    if n % 2 == 0:
        return False
        
#Ask user for number.

n = int(input("Enter a number?"))

#call function and print the result

if is_prime():
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")