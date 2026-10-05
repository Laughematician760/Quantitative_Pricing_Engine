#geometric_brownian_motion
import numpy as np

#Step 1: Define the variables and constants
trading_days = 252
dt = 1/trading_days
S_0 = 100
annualized_drift = .08
annualized_volatility = .2

t_coefficient = (annualized_drift - (annualized_volatility*annualized_volatility)/2)

#Step 2: Define the matrices
weiner_matrix = np.random.normal(0, 1, size=(10000, trading_days))

shock_matrix = np.sqrt(dt)*weiner_matrix

cumulative_matrix = np.cumsum(shock_matrix, axis = 1)

time_array = np.arange(1/trading_days, 1+1/trading_days, 1/trading_days)


#Step 3: Combine the needed terms
first_ito_term = t_coefficient*time_array
second_ito_term = annualized_volatility*cumulative_matrix



#Step 4: Ito's Solution

S_t = S_0*np.exp(first_ito_term + second_ito_term)


#European Call Option Add-On

K = 105
max_vector = np.maximum(0, S_t[:, 251]-K)

fair_price = np.mean(max_vector) * np.exp(-annualized_drift * 1)

print(fair_price)










