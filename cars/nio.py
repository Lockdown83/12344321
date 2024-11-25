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
        # A class variable to keep track of the number of Nio cars created
        car_count = 0

        def __init__(self, model, battery_capacity, range_per_charge, price):
            """
            Initializes the Nio car with the given attributes and increments the car count.

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
            
            # Increment the car count each time a new Nio car is created
            Nio.car_count += 1

        @classmethod
        def count_cars(cls):
            """
            Returns the total number of Nio cars created.

            Returns:
            int: The total number of Nio cars.
            """
            return cls.car_count