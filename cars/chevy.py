def chevy_bolt_ev_specs():
    specs = {
        "Model": "Chevy Bolt EV",
        "Type": "Electric Vehicle",
        "Battery Capacity": "66 kWh",
        "Range": "259 miles",
        "Horsepower": "200 hp",
        "Torque": "266 lb-ft",
        "Charging Time (Level 2)": "7 hours",
        "Fast Charging": "DC Fast Charging capable",
        "Seating Capacity": 5,
        "Cargo Space": "16.6 cubic feet"
    }
    
    print("Chevy Bolt EV Specifications:")
    for key, value in specs.items():
        print(f"{key}: {value}")  # Print each specification

# Example usage:
# chevy_bolt_ev_specs()  # This will print the specifications of the Chevy Bolt EV
