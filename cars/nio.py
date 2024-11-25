class Nio:
    """
    A class to represent the Nio electric car brand from China.

    Attributes:
    model (str): The model of the car.
    battery_capacity (float): The battery capacity in kWh.
    range_per_charge (float): The range of the car on a full charge in kilometers.
    price (float): The price of the car in dollars.
    """

    def __init__(self, model, battery_capacity, range_per_charge, price):
        """
        Initializes the Nio car with the given attributes.

        Parameters:
        model (str): The model of the car.
        battery_capacity (float): The battery capacity in kWh.
        range_per_charge (float): The range of the car on a full charge in kilometers.
        price (float): The price of the car in dollars.
        """
        self.model = model
        self.battery_capacity = battery_capacity
        self.range_per_charge = range_per_charge
        self.price = price
