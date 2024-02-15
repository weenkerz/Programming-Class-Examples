import itertools as it
import random

num = [random.randint(-5, 10) for i in range(16)] # Generate a list of 15 random integers ranging from -5 to 10
print(num) # Show what the list of numbers is
target = int(input("Please enter the target number: ")) # Ask for a number to search for sums
finale = [] # Create an empty list to store the final results in

num_per = list(it.permutations(num, 2)) # Create a list of tuples of all permutations of 2 variables in num
for i in num_per:
    if i[0] + i[1] == target and i not in finale and i[::-1] not in finale: # Check to see if the numbers in each tuple
        finale.append(i)                                                    # add up to the target and put it in the
                                                                            # finale list if it's not in already
print(finale)
