#import library
import numpy as np

import math

#single period binomial model
def price_call_option(S, u, d, K, r):
    p = (1+r-d)/(u-d)
    u_terminal_payout = max(S*u-K, 0)
    d_terminal_payout = max(S*d-K, 0)
    return (u_terminal_payout*p + d_terminal_payout*(1-p))/(1+r)



#Multi-period model

def price_call_option_multi_period(S, u, d, K, r, N):
    # Phase 1: Terminal State Generation
    p = (1 + r - d) / (u - d)
    u_exp_list = np.arange(N + 1)
    d_exp_list = N - u_exp_list
    
    # Vectorized calculation of all N+1 terminal stock prices
    S_T = S * (u ** u_exp_list) * (d ** d_exp_list)
    
    # Vectorized calculation of terminal Call Option payouts
    P = np.maximum(S_T - K, 0)
    
    # Phase 2: Vectorized Backward Induction
    for i in range(N):
        # Calculate the discounted expected value for the entire period simultaneously
        P = (p * P[1:] + (1 - p) * P[:-1]) / (1 + r)
        
    return P[0]

# --- Testing the Engine ---
# Baseline Parameters: S=100, u=1.20, d=0.90, K=100, r=0.05
print(f"1-Period Price: {price_call_option_multi_period(100, 1.20, 0.90, 100, 0.05, 1):.4f}")
print(f"3-Period Price: {price_call_option_multi_period(100, 1.20, 0.90, 100, 0.05, 3):.4f}")
print(f"1000-Period Price: {price_call_option_multi_period(100, 1.20, 0.90, 100, 0.05, 1000):.4f}")

#Cox-Ross-Rubenstein wrapper function

def price_call_option_crr(S, K, T, r, sigma, N):
    delta_t = T/N
    u = math.exp(sigma*math.sqrt(delta_t))
    d = math.exp(-sigma*math.sqrt(delta_t))
    cc_rate_step = math.exp(r*delta_t)-1

    return price_call_option_multi_period(S, u, d, K, cc_rate_step, N)


print(price_call_option_crr(100, 100, 1, .05, .20, 1000))
