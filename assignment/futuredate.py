from datetime import datetime

# Input future date-time
future_str = input("Enter future date-time (YYYY-MM-DD HH:MM:SS): ")

# Convert to datetime
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

# Current time
now = datetime.now()

# Difference
time_remaining = future_time - now

# Extract components
days = time_remaining.days
seconds = time_remaining.seconds

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Remaining time: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")