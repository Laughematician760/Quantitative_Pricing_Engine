import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

##########Exercise 1: "Using your answer to Blitzstein 5.17, turn one million Uniform draws into draws with the CDF of that exercise. Find the fraction below 1."##########

rng = np.random.default_rng(1)

U = rng.random(1000000)

X = (-np.log(1-U))**(1/3)

X_below_one = (X < 1).mean()

print("Task 1:", X_below_one, 1 - 1/np.exp(1))

##########Exercise 2: "Do the same for the Logistic CDF of Example 5.3.4. Find the fraction below 1. Plot a histogram with the density drawn over it." ##########

logistic_X = np.log(U/(1-U))

logistic_X_below_one = (logistic_X < 1).mean()

print("Task 2:", logistic_X_below_one, np.exp(1)/(1 + np.exp(1)))




##########Exercise 3: "Draw one million standard Normal values. Find the mean, the variance, and the fractions within 1, 2 and 3 of zero. Then answer Zhou 7.3 "Monte Carlo simulation" part B in a comment." ##########

Z = rng.standard_normal(1000000)

normal_mean = Z.mean()

normal_variance = Z.var()

fraction_one = (np.abs(Z) < 1).mean()

fraction_two = (np.abs(Z) < 2).mean()

fraction_three = (np.abs(Z) < 3).mean()

print("Task 3:", normal_mean, 0)
print("Task 3:", normal_variance, 1)

print("Task 3:", fraction_one, 0.683)
print("Task 3:",fraction_two, 0.954)
print("Task 3:",fraction_three, 0.997)


#Zhou 7.3 Part B asks how to generate N(\mu, \sigma^2) if your computer can only generate values in [0, 1] uniformly? The answer is the use the Theorem of the universality
# of the uniform distribution and then create a random variable Z that generates Z ~ N(0, 1) values by using the computed inverse \Phi^{-1}(c). Then you can use the location-scaling principle to obtain \mu + \sigma Z
# N(\mu, \sigma^2) random variable. 





##########Exercise 4: "Find the 2.5%, 50% and 97.5% quantiles of the draws in task 3." ##########

twopfive = np.quantile(Z, .025)

fifty = np.quantile(Z, .5)

ninety_sevenp_five = np.quantile(Z, .975)

print("Task 4:", twopfive, -1.96)
print("Task 4:", fifty, 0)
print("Task 4:", ninety_sevenp_five, 1.96)


##########Exercise 5: "Form X = 3 + 2Z from the draws in task 3. Find the fraction of X below 4 and compare it with the exact value." ##########

transformed_normal = 2*Z + 3

fraction_four = (transformed_normal < 4).mean()

print("Task 5:", fraction_four, norm.cdf(.5))











##########Exercise 6: "Check your formula from Blitzstein 5.37 against a simulation at c = 0.7 and at c = −1." ##########



##########Exercise 7: "Build an array of shape (100000, 12) of Uniform draws and sum each row. Find the mean, the variance, and the 5% and 95% quantiles of the row sums. Plot a histogram." ##########

matrix = rng.random((100000, 12))

row_sum = matrix.sum(axis =1)

mean = row_sum.mean()

variance = row_sum.var()

five_quantile = np.quantile(row_sum, .05)

ninety_five_quantile = np.quantile(row_sum, .95)

print("Task 7:", mean , 6)
print("Task 7:", variance , 1)
print("Task 7:", five_quantile , norm.ppf(.05, 6, 1))
print("Task 7:", ninety_five_quantile, norm.ppf(.95, 6, 1))



##########Exercise 8: "Write task 7 with a Python loop over the rows, then time both versions." ##########



##########Plotting##########
plt.figure
plt.hist(logistic_X, bins=100, density=True)        # logistic_X = Logistic draws
x = np.linspace(-8, 8, 400)
plt.plot(x, np.exp(x) / (1 + np.exp(x))**2)  # the Logistic density


plt.figure()
plt.hist(row_sum, bins = 100, density = True)
x = np.linspace(2, 10, 100000)
plt.plot(x, norm.pdf(x, 6, 1))
plt.show()
