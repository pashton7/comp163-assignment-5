# GITHUB LINK

# Challenge 1: Collatz conjecture sequence
current_number = int(input("Enter starting number: ")) # Require user input of number
step_count = 0 # count each step the loop makes

print("Sequence: ", end=" ") # Print the line that will hold the sequence of numbers
while current_number != 1: # Use a while loop because the exact amount of times needed to be looped is unknown
    print(current_number, end=" ")
    if current_number % 2 == 0: # Checks to see if int is even if its divisible by 2
        current_number //= 2 # Use double slahses to keep the number an int
    else: # If number is not divisible by two then it has to be an odd number
        current_number *= 3
        current_number += 1
    step_count += 1 # incriment steps
print(current_number) # print final result
print(f"Steps: {step_count}") # Print how many steps were needed

# Challenge 2: Prime number checker
current_number = int(input("Enter number: ")) # Require user input of number - re-use old variable since theres no reason for a new one

print(f"Testing divisors from 2 to {current_number-1}")
for num in range(2, current_number-1): # We know how many times we want/need to loop so we use a FOR loop
    if (current_number % num == 0): # If the divisor leaves a remainder of 0 then the number is not prime
        print(f"{current_number} is not prime (divisible by {num})")
        break # Break the loop since we know the number is not prime
else: # If the FOR loop doesn't break then the number is prime
    print(f"{current_number} is prime!")

# Challenge 3: Multiplication Table Grid
print("Multiplication Table:") # Print the table title
print("     1   2   3   4   5   6   7   8   9  10") # Print the column numbers
for row in range(1,11): # Loop through each row 1-10
    print(f"{row:2}", end="") # Print the row number at the start of the line
    for column in range(1, 11): # Loop through each column number 1-10
        product = column * row # Calculate the row number by the column number
        print(f"{product:4}", end="") # Print the product on the same line as its respective row
    print() # Create a new line for the next row
