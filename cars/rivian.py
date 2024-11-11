# The following code defines a function that prints the specifications of a Rivian truck.
def print_rivian_truck_specs():
    """
    Print the specifications of a Rivian truck.
    """
    specs = {
        "Model": "Rivian R1T",
        "Battery Capacity": "105 kWh to 180 kWh",
        "Range": "314 miles (with 180 kWh battery)",
        "Horsepower": "Up to 750 hp",
        "Torque": "Up to 829 lb-ft",
        "Towing Capacity": "Up to 11,000 lbs",
        "Acceleration": "0-60 mph in 3 seconds",
        "Drive": "All-wheel drive",
        "Seating Capacity": "5 passengers",
        "Cargo Space": "Up to 62 cubic feet"
    }

    print("Rivian Truck Specifications:")
    for key, value in specs.items():
        print(f"{key}: {value}")  # Print each specification in a readable format

# Example usage:
# print_rivian_truck_specs()  # This will print the specifications of the Rivian truck
