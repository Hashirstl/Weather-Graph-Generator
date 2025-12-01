import matplotlib.pyplot as plt

# Get the number of days and temperature data
num_days = int(input("Enter number of days: "))

x_axis = [f"{i+1}" for i in range(num_days)]

y_axis = []
for i in range(num_days):
    value = float(input(f"Enter temperature for day {i+1}: "))
    y_axis.append(value)

# Find the highest and lowest temperatures
highest_temp = max(y_axis)
lowest_temp = min(y_axis)

# Create the plot
plt.plot(x_axis, y_axis, marker='o', linestyle='-', color='b')

# Add horizontal lines for highest and lowest temperatures
plt.axhline(y=highest_temp, color='r', linestyle='--', label=f"Highest Temp ({highest_temp}°C)")
plt.axhline(y=lowest_temp, color='g', linestyle='--', label=f"Lowest Temp ({lowest_temp}°C)")

# Customize the plot
plt.xlim(-0.25, num_days - 0.25)
plt.ylim(0, 60)  # Fixed Y-axis from 0 to 60
plt.yticks(range(0, 61, 2))

plt.xlabel("Days")
plt.ylabel("Temperature in (°C)")
plt.title("Weather Graph")

# Add a legend to describe the lines
plt.legend()

# Show the plot
plt.show()
