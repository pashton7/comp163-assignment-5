# GITHUB LINK

# Collatz conjecture sequence
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