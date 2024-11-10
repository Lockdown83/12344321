# Vega is a measure of the sensitivity of the price of an option to changes in the volatility of the underlying asset. 
# It is one of the "Greeks" used in options trading. The mathematical representation of Vega can be expressed as:

def calculate_vega(S, K, T, r, sigma):
    """
    Calculate the Vega of a European call option.

    Parameters:
    S (float): Current stock price
    K (float): Strike price of the option
    T (float): Time to expiration in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset

    Returns:
    float: Vega of the option
    """
    from math import exp, sqrt, pi

    # Calculate d1 using the Black-Scholes formula components
    d1 = (log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * sqrt(T))
    
    # Vega formula
    vega = S * exp(-d1**2 / 2) / sqrt(2 * pi) * sqrt(T)
    
    return vega
