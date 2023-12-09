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

        # Convert the API response data into a dictionary with date as key and rating as value
        data_dict = {}
        for point in data_points:
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


    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching rating history for player {username} from Lichess API: {e}")

    return {"points": csv_data}
    # return {"username": username, "points": last_30_days_data}





# Example route to fetch a CSV file with the rating history for the top 50 players
@app.get("/players/rating-history-csv", response_class=Response)
def get_rating_history_csv():
    try:
        # first fetching the list of top 50 players and extracting users array from it
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



@app.get("/players/rating-history-csv2", response_class=Response)
def get_rating_history_csv():
    try:
        # first fetching the list of top 50 players and extracting users array from it
        top_players_response = get_top_players()
        # print(top_players_response.get("top_players"))
        top_players_data = [player[1] for player in top_players_response["top_players"]]
        # print(top_players_data)           # list of username of top players

        # Prepare CSV data
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)

        # Extract dates from points array
        dates_points = get_rating_history(top_players_data[0]).get("points")
        # print(dates_points)
        dates = [point[0] for point in dates_points]

        # Write CSV header
        header_data = ["username"]
        header_data.extend(dates) 
        # print(header_data);
        csv_writer.writerow(header_data)

        # Fetch rating history for each top player
        # evaluating list of ratings for each user along with username at front for the last 30 days
        for user in top_players_data:
            player_rating_history = get_rating_history(user).get("points")
            # print(player_rating_history)
            current_row = [user]
            ratings = [player_rating[1] for player_rating in player_rating_history]
            current_row.extend(ratings)

            # Write player data to CSV
            csv_writer.writerow(current_row)

        # Set up response with CSV data
        response = Response(content=csv_data.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"

        return response

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Lichess API: {e}")