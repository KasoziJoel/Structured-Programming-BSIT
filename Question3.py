
n = int(input("Enter a positive number"))

if n <= 0:
    print("Please enter a number greater than zero")

else:
    even_sum = 0

#loop for numbers from 1 to n
    
    for n in range(2, n+1):
        if n % 2 == 0:
            even_sum += n

    print(f"The sum of even numbers from 2 to {n} is {even_sum}")




