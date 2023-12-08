from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
import threading
from io import StringIO
import csv
from datetime import datetime, timedelta

# Create an instance of the FastAPI class
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) for your FastAPI app
origins = [
    "http://localhost",
    "http://localhost:3000",  # Replace with your React app's URL during development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





# URL for the Lichess API to get the top 50 classical chess players
top_players_url = "https://lichess.org/api/player/top/50/classical"

# URL for the Lichess API to get the 30-day rating history for a specified player
rating_history_url = "https://lichess.org/api/user/{username}/rating-history"





# Backend Home EndPoint Test link
@app.get("/", response_model=dict)
def get_home():
    return {"message": "Welcome to ReachHub's Lichess.org API services! \n\nRead the documentation here for more details: \nLink: https://github.com/pranjal-barnwal/reach-hub/readme.md"}

    




# Example route to fetch the top 50 classical chess players
# will give: [id, username, rating] for each of the user in array form sequentially
@app.get("/top-players", response_model=dict)
def get_top_players():
    try:
        top_players_response = requests.get(top_players_url)
        top_players_data = top_players_response.json().get("users")

        # Extracting id, username and rating information
        top_player_usernames = [(user["id"], user["username"], user["perfs"]["classical"]["rating"]) for user in top_players_data]


    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top players from Lichess API: {e}")

    return {"top_players": top_player_usernames}






# Example route to fetch the 30-day rating history for a specified player
@app.get("/player/{username}/rating-history", response_model=dict)
def get_rating_history(username: str):
    try:
        player_rating_history_url = rating_history_url.format(username=username)
        rating_history_response = requests.get(player_rating_history_url)
        rating_history_data = rating_history_response.json()

        data_points = None
        for entry in rating_history_data:
            if entry.get('name') == 'Classical':
                data_points = entry.get('points', [])

        print(type(data_points))
        print(data_points)
        print(type(data_points[0][0]))
        print(type(data_points[0][1]))
        print(type(data_points[0][2]))
        print(type(data_points[0][3]))


        # Convert the JSON data points to Python datetime objects
        dates = [datetime(item[0], item[1]+1, item[2]) for item in data_points]
        # dates = [datetime(item[0], item[1], item[2]) for item in data_points]

        # Get today's date
        today = datetime.now()
        today = today.replace(month=today.month)

        # Calculate the date 30 days ago from today
        thirty_days_ago = today - timedelta(days=30)

        # Filter data for the last 30 days
        last_30_days_data = [data_points[i] for i, date in enumerate(dates) if date >= thirty_days_ago]


    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching rating history for player {username} from Lichess API: {e}")

    return {"username": username, "points": last_30_days_data}
    # return {"username": username, "points": username}
    # return {"username": username, "points": data_points}





# Example route to fetch a CSV file with the rating history for the top 50 players
@app.get("/players/rating-history-csv", response_class=Response)
def get_rating_history_csv():
    try:
        top_players_response = requests.get(top_players_url)
        top_players_data = top_players_response.json().get("users")

        # Prepare CSV data
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)

        # Write CSV header
        csv_writer.writerow(["Username", "Rating 30 Days Ago", "Rating Today"])

        # Fetch rating history for each top player
        for user in top_players_data:
            username = user.get("username")
            player_rating_history_url = rating_history_url.format(username=username)
            rating_history_response = requests.get(player_rating_history_url)
            rating_history_data = rating_history_response.json()

            # Extract rating from 30 days ago and today
            rating_30_days_ago = rating_history_data[-30].get("rating", "N/A") if len(rating_history_data) >= 30 else "N/A"
            rating_today = rating_history_data[-1].get("rating", "N/A")

            # Write player data to CSV
            csv_writer.writerow([username, rating_30_days_ago, rating_today])

        # Set up response with CSV data
        response = Response(content=csv_data.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"

        return response

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Lichess API: {e}")