# Rho is a measure of the sensitivity of the price of an option to changes in the risk-free interest rate. 
# It indicates how much the price of an option will change for a 1% change in interest rates. 
# The mathematical representation of Rho for a European call option can be expressed as:

def calculate_rho(S, K, T, r, sigma):
    """
    Calculate the Rho of a European call option.

    Parameters:
    S (float): Current stock price
    K (float): Strike price of the option
    T (float): Time to expiration in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset

    Returns:
    float: Rho of the option
    """
    from math import exp, sqrt

    # Calculate d1 using the Black-Scholes formula components
    d1 = (log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * sqrt(T))
    
    # Rho formula for a European call option
    rho = K * T * exp(-r * T) * norm.cdf(d1)
    
    return rho
