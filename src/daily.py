import io

"""
This program asks the user for n number of stairs and computes how many different combinations 
of 1 or 2 steps  to ascend the staircase
"""

def staircase(n):
    """
    This function solves how many combinations to ascend n steps either taking 1 or 2 steps at a time.
    Uses recursion and is very slow.
    """
    if n <= 1:
        return 1
    return staircase(n-1) + staircase(n-2)

def staircaseUsingLoop(n):
    """
    This function solves the same problem as above, but utilizes a loop to iterate through the range of n and returns the answer
    """
    a, b = 1, 2
    
    for r in range(n-1):
        a, b = b, a+b
    
    return a



print("\n========================================")
print("             Stair Ascender             ")
print("========================================\n")
print("This program will ask for a number of steps from user")
print("and will compute how many combinations to ascend the set")
print("taking either 1 or 2 steps at a time.\n")
print("========================================")

# Prime loop for program
tryAgain = True
while tryAgain:
    # Gather input
    numeric = False
    while not numeric:
        n = input("\nEnter the number of steps in the staircase: ")
        numeric = n.isnumeric()

        if not numeric:
            print("Number of steps must be a number, please try again\n")
            
    # Select method to use
    valid = False
    while not valid:
        method = input("\nSelect either [R] recursive or [L] loop method: ")
        method = method.upper() 

        if (method == 'R' or method == 'L'):
            valid = True
        else:
            print("\nInvalid selection, please try again.")

    if (method == 'R'):
        print("\nComputing...")
        print("\nThere are " + str(staircase(int(n))) + " combinations of climbing " + str(n) + " stairs.")

    elif (method == 'L'):
        print("There are " + str(staircaseUsingLoop(int(n))) + " combinations of climbing " + str(n) + " stairs.")
    
    # Ask to try again
    again = ''
    while (again != 'Y' and again != 'N'):
        again = input("\nWould you like to try another scenario? [Y] yes or [N] no: ")
        again = again.upper()

        if (again == 'N'):
            tryAgain = False



