# Define the probabilities
p_A = 1 / 7
p_B = 2 / 7
p_C = 4 / 7
p_D_given_A = 0.005

# Calculate the denominator using the law of total probability
p_D = p_D_given_A * p_A + 0.008 * p_B + 0.010 * p_C

# Calculate the probability that a defective pipe came from plant A using Bayes' Theorem
p_A_given_D = (p_D_given_A * p_A) / p_D

# Convert the probability to an irreducible fraction
from fractions import Fraction
result_fraction = Fraction(p_A_given_D).limit_denominator()

# Print the result in the required format
print(f"{result_fraction.numerator}/{result_fraction.denominator}")
