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

        print("CSV DATA:")
        print(csv_data)
        # Convert CSV data to string format
        csv_data_str = csv_data.getvalue()
        print("CSV DATA STR:")
        print(csv_data_str)
        # Save the CSV data to the SQL Database
        saveCsv(csv_data_str)

        # Set up response with CSV data
        response = Response(content=csv_data_str, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=rating_history.csv"
        return response

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Lichess API: {e}")