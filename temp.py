from datetime import datetime, timedelta

# Your JSON data points
data_points = [
    [2023, 10, 8, 2144],
    [2023, 10, 9, 2961],
    [2023, 10, 11, 2962],
    [2023, 11, 4, 2962],
    [2023, 11, 9, 2963],
]
print(type(data_points))

# Convert the JSON data points to Python datetime objects
dates = [datetime(item[0], item[1], item[2]) for item in data_points]
# months range from 0-11, so incremented by 1

# Get today's date
today = datetime.now()
today = today.replace(month=today.month - 1)

# Calculate the date 30 days ago from today
thirty_days_ago = today - timedelta(days=30)

# Filter data for the last 30 days
last_30_days_data = [data_points[i] for i, date in enumerate(dates) if date >= thirty_days_ago]

# Printing the filtered data for the last 30 days
print(last_30_days_data)
