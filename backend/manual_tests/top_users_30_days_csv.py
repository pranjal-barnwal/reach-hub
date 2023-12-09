# from fastapi import FastAPI, HTTPException, Response
# from fastapi.middleware.cors import CORSMiddleware
# import requests
# import threading
# from io import StringIO
# import csv
# from datetime import datetime, timedelta

# # URL for the Lichess API to get the top 50 classical chess players
# top_players_url = "https://lichess.org/api/player/top/50/classical"

# # URL for the Lichess API to get the 30-day rating history for a specified player
# rating_history_url = "https://lichess.org/api/user/{username}/rating-history"



# top_players_response = requests.get(top_players_url)
# top_players_data = top_players_response.json().get("users")

# # Prepare CSV data
# csv_data = StringIO()
# csv_writer = csv.writer(csv_data)

# # Write CSV header
# csv_writer.writerow(["Username", "Rating 30 Days Ago", "Rating Today"])

# # Fetch rating history for each top player
# for user in top_players_data:
#     username = user.get("username")
#     player_rating_history_url = rating_history_url.format(username=username)
#     rating_history_response = requests.get(player_rating_history_url)
#     rating_history_data = rating_history_response.json()

#     # Extract rating from 30 days ago and today
#     rating_30_days_ago = rating_history_data[-30].get("rating", "N/A") if len(rating_history_data) >= 30 else "N/A"
#     rating_today = rating_history_data[-1].get("rating", "N/A")

#     # Write player data to CSV
#     csv_writer.writerow([username, rating_30_days_ago, rating_today])

# # Set up response with CSV data
# response = Response(content=csv_data.getvalue(), media_type="text/csv")
# response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"

# print(response)


api_result = {
    "points": [
        ["09-11-2023", None],
        ["10-11-2023", 2532],
        ["11-11-2023", 2544],
        ["12-11-2023", 2544],
        ["13-11-2023", 2544],
        ["14-11-2023", 2544],
        ["15-11-2023", 2544]
    ]
}

# Extract dates from points array
dates = [point[0] for point in api_result["points"]]

print(dates)