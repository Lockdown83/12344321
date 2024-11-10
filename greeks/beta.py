# Beta is a measure of the volatility, or systematic risk, of a security or portfolio in comparison to the market as a whole. 
# It indicates how much the price of a stock is expected to move in relation to market movements. 
# The mathematical representation of Beta can be expressed as:

def calculate_beta(stock_returns, market_returns):
    """
    Calculate the Beta of a stock using historical returns.

    Parameters:
    stock_returns (list of float): Historical returns of the stock
    market_returns (list of float): Historical returns of the market

    Returns:
    float: Beta of the stock
    """
    from numpy import cov, var

    # Calculate covariance between stock returns and market returns
    covariance = cov(stock_returns, market_returns)[0][1]
    
    # Calculate variance of market returns
    market_variance = var(market_returns)

    if market_variance == 0:
        raise ValueError("Market variance cannot be zero.")
    
    # Beta formula
    beta = covariance / market_variance
    return beta

