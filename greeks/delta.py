# Start Generation Here
# Delta is a measure of how much an option's price is expected to change when the price of the underlying asset changes by $1. 
# In options trading, delta values range from 0 to 1 for call options and -1 to 0 for put options. 
# A delta of 0.5, for example, indicates that if the underlying asset increases by $1, the option's price is expected to increase by $0.50.
# This metric helps traders understand the sensitivity of an option's price to changes in the underlying asset's price.
# End Generation Here
def calculate_delta(option_price_change, underlying_price_change):
    """
    Calculate the delta of an option.

    Parameters:
    option_price_change (float): The change in the option's price.
    underlying_price_change (float): The change in the underlying asset's price.

    Returns:
    float: The delta of the option.
    """
    if underlying_price_change == 0:
        raise ValueError("Underlying price change cannot be zero.")
    
    delta = option_price_change / underlying_price_change
    return delta

# Example usage:
# Assuming the option price changes by $0.50 when the underlying asset changes by $1.00
delta_value = calculate_delta(0.50, 1.00)
print(f"The delta of the option is: {delta_value}")
