# This function prints numbers from 1 to n, replacing multiples of 3 with "Fizz",
# multiples of 5 with "Buzz", and numbers divisible by both with "FizzBuzz".

# Define a function named fizz_buzz. The type hint `n: int` indicates
# that n is expected to be a whole number; Python does not enforce it.
def fizz_buzz(n: int):
    # Loop from 1 through n. range stops BEFORE its second argument,
    # so n + 1 makes sure n is included. i is the current number.
    for i in range(1, n + 1):
        # % gives the remainder after division. A remainder of 0 means
        # the number divides evenly. `and` requires both checks to be true.
        # Check both first, so numbers like 15 print "FizzBuzz".
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # elif means "otherwise, if". This runs only if the first check failed.
        elif i % 3 == 0:
            print("Fizz")
        # If the earlier checks failed, check whether i divides evenly by 5.
        elif i % 5 == 0:
            print("Buzz")
        # If none of the checks matched, print the number itself.
        else:
            print(i)


# Run this block only when you run this file directly, for example:
# python fizzBuzz.py
# Importing the function from another file will not run this block.
if __name__ == "__main__":
    # Call the function with n = 12. Keep this OUTSIDE the function:
    # calling fizz_buzz(15) inside itself would repeatedly call it again.
    fizz_buzz(12)
