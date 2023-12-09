from datetime import datetime, timedelta
import csv

# Sample API response
api_response = {
    "username": "Apodex64",
    "points": [
        [2023, 10, 10, 2532],
        [2023, 10, 11, 2544],
        [2023, 10, 13, 2525]
    ]
}

# Convert the API response data into a dictionary with date as key and rating as value
data_dict = {}
for point in api_response['points']:
    date_str = f"{point[2]:02d}-{point[1]+1:02d}-{point[0]}"
    data_dict[date_str] = point[3]

# Get the date range for the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Create CSV data for each date with the corresponding rating or the last available rating
csv_data = []
last_rating = None
for date in date_range:
    date_str = date.strftime("%d-%m-%Y")
    rating = data_dict.get(date_str, last_rating)
    if rating is not None:
        last_rating = rating
    csv_data.append([date_str, rating])

print(csv_data)
# Write the CSV data to a file
with open('last_30_days_ratings.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Rating'])
    writer.writerows(csv_data)

print("CSV file for the last 30 days generated successfully.")
