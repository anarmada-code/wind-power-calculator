# Wind Power Calculator

print("===== WIND POWER CALCULATOR =====")

# Get inputs from user
wind_speed = float(input("Enter wind speed (m/s): "))
blade_radius = float(input("Enter blade radius (m): "))
efficiency = float(input("Enter turbine efficiency (%): "))

# Constants
air_density = 1.225

# Calculate swept area
area = 3.14159 * blade_radius ** 2

# Convert efficiency from percentage to decimal
efficiency = efficiency / 100

# Calculate wind power
power = 0.5 * air_density * area * wind_speed ** 3 * efficiency

# Convert watts to kilowatts
power_kw = power / 1000

# Display results
print("\n===== RESULT =====")
print(f"Swept Area: {area:.2f} m²")
print(f"Estimated Power: {power:.2f} W")
print(f"Estimated Power: {power_kw:.2f} kW")
