def discounted_cash_flow(cash_flows, discount_rate):
    """
    Calculate the discounted cash flow (DCF) for a series of cash flows.

    Parameters:
    cash_flows (list of float): A list of cash flows for each period.
    discount_rate (float): The discount rate as a decimal (e.g., 0.1 for 10%).

    Returns:
    float: The present value of the cash flows.
    """
    dcf = 0
    for t, cash_flow in enumerate(cash_flows):
        dcf += cash_flow / (1 + discount_rate) ** t
    return dcf

# Example usage:
# Let's assume we have projected cash flows for the next 5 years for Ford.
projected_cash_flows = [50000, 55000, 60000, 65000, 70000]  # Example cash flows in dollars
discount_rate = 0.1  # 10% discount rate

# Calculate the DCF
dcf_value = discounted_cash_flow(projected_cash_flows, discount_rate)
print(f"The discounted cash flow (DCF) value for Ford is approximately ${dcf_value:.2f}.")
