import math


# Function takes an int
# Returns a list of the ints factors including itself as floats
def get_factors(number):
    half_factors = []
    factors = []
    for potentialFactor in range(1, int(math.sqrt(abs(number))) + 1):
        if number % potentialFactor == 0:
            half_factors.append(potentialFactor)
    size = len(half_factors)
    for i in range(size):
        factors.append(float(half_factors[i]))
    for factor in range(size):
        fact = number / half_factors[factor]
        if fact in factors:
            pass
        else:
            factors.append(fact)
    return factors


# Function takes int argument
# Returns True if the int is prime, False if not
def is_it_prime(number):
    return len(get_factors(number)) == 2    


# Function takes an int, n digits long
# Returns a list of length n of all its digits
def find_digits(number):
    digits = [int(x) for x in str(number)]
    return digits


# Function takes list of digits
# Returns a single int with corresponding digits
def find_number(digits):
    number = int("".join(map(str, list)))
    return number


# Function takes a positive integer
# Returns True if palindromic
def is_it_palindromic(number):
    digit = find_digits(number)
    return digit == digit[::-1]


# Function takes a positive integer
# Returns the factorial of the input as an int
def find_factorial(number):
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    return factorial


# Function takes a list of digits
# Returns all circular permutations as list of a list
def find_circular_perms(digits):
    all_perms = []
    all_perms.append(digits)
    for i in range(len(digits)-1):
        new_perm = digits[i+1:] + digits[:i+1]
        all_perms.append(new_perm)
    return all_perms
