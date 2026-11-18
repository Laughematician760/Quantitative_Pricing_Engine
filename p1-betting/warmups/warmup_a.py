import numpy as np

#COME BACK AND WRITE UP THE APPROPRIATE SPECS FOR EACH FUNCTION


#########Exercise 1: "Build the integers 1 to 100. Find the sum of their squares, and the sum of those divisible by 3 or by 5." ##############


#Builds the integers 1, ..., 100
first_hundred_integers = np.arange(1, 101, 1)

#Input: Array of the first 100 integers
#Output: The integer that is the sum of the squares of all of the numbers in the list 1, ..., 100
def sum_of_squares(num_array):
    return sum([x*x for x in num_array])

#Input: Array of the first 100 integers
#Output: The integer that  is the value of the sum of all integers in the list 1, ... , 100 divisible by either 3 or 5
def sum_div_by_three_or_five(num_array):
    return sum([x for x in num_array if x % 3 == 0 or x % 5 == 0])


##########Exercise 2: "Build the integers 0 to 11 as a 3 by 4 array. Find the row sums and the column sums. Subtract each column's mean from that column." ##########

first_twelve_ints = np.arange(0, 12, 1)

twelve_array = np.reshape(first_twelve_ints, (3, 4))

def row_sums(num_array):
    return np.sum(num_array, axis = 1)

def column_sums(num_array):
    return np.sums(num_array, axis = 0)

def mean_adjusted_columns(num_array):
    return num_array - np.mean(num_array, axis = 0)



##########Exercise 3: "Draw one million Uniform(0, 1) values. Find the fraction lying between 0.2 and 0.5, and the mean of the values in that range." ##########

rng = np.random.default_rng(1)
U = rng.random(1000000)

def ranged_fraction(num_array):
    return len([x for x in num_array if x > .2 and x < .5])/(1000000)

def ranged_mean(num_array):
    return np.mean([x for x in num_array if x > .2 and x < .5])



##########Exercise 4: Roll two dice 100,000 times as one array of shape (100000, 2). Find the fraction of rolls with sum 7, and the fraction whose larger die is a 6.##########
rng = np.random.default_rng(1)
die_roll_vals = rng.integers(1, 7, (100000, 2))

def seven_fraction(num_array):
    return len([x for x in np.sum(num_array, axis = 1) if x == 7])/(100000)

def six_is_max(num_array):
    return len([x for x in np.max(num_array, axis = 1) if x == 6])/(100000)



##########Exercise 5: "Start with wealth 1 and apply the factors 1.1, 0.9, 1.1, 0.9 and so on, ten factors in all. Produce the whole wealth path."##########
factor_reps = np.tile([1.1, .9], 5) 

wealth_path = np.cumprod(factor_reps)


##########Exercise 6:"Simulate 100,000 walks of 50 steps, each step +1 or −1 with equal probability. Find the fraction ending at 6 or higher, and the fraction ending at least 6 away from 0."##########

rng = np.random.default_rng(1)
random_walk_trials = rng.choice([-1, 1], (100000, 50))

end_result = np.cumsum(random_walk_trials, axis = 1)

fraction_bigger_than_six = len([x for x in end_result[:, 49] if x >= 6])/100000

abs_bigger_than_six = len([x for x in np.abs(end_result[:, 49]) if x >= 6])/100000


##########Exercise 7: ""







    





