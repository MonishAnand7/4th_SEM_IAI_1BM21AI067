# Enter your code here. Read input from STDIN. Print output to STDOUT

# Define the total number of outcomes when rolling two dice
total_outcomes = 6 * 6  # 6 sides on each die

# Define the number of favorable outcomes
favorable_outcomes = 0

# Iterate through all possible outcomes
for die1 in range(1, 7):
    for die2 in range(1, 7):
        # Check if the values are different and their sum is 6
        if die1 != die2 and die1 + die2 == 6:
            favorable_outcomes += 1

# Calculate the probability as a fraction
from fractions import Fraction
probability = Fraction(favorable_outcomes, total_outcomes)

# Print the result in the required format
print(f"{probability.numerator}/{probability.denominator}")
