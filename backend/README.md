# Custom Lichess Backend with FastAPI & PostgreSQL
by ReachHub: [Pranjal Kumar](https://linkedin.com/in/pranjal-barnwal)

## Requirements
- PostgreSQL
- Python

## Set up
```bash
# moving to the backend folder
cd .\backend\ 

# installing all the dependencies
pip i

# activating virtual environment script
.\env\Scripts\activate

# running app of main.py for server
uvicorn main:app --reload
```



## Sample Data
- [Top Player Data](###top-players-data)
- [Rating History for player](###rating-history-for-player)
- [Rating History CSV](###rating-history-csv)


### Top Players Data
This endpoint returns array of top players details. Each including: `id`, `username` & `rating`
> **Reference:** https://lichess.org/api/player/top/50/classical

**Endpoint:** `/top-players`

```json
{
  "top_players": [
    ["apodex64", "Apodex64", 2555],
    ["unkreativ3", "Unkreativ3", 2535],
    ["josip_buje", "Josip_buje", 2534],
    ...
  ]
}
# [id, username, rating]
```





### Rating History for player
This Endpoint will return last 30 dates ratings for the mentioned user
> **Reference:** https://lichess.org/api/user/{username}/rating-history/classical

For dates where no-rating is mentioned, we copied the last available data.

**Endpoint:** `/player/{username}/rating-history`
```json
{
  "points": [
    ["09-11-2023", 0],
    ["10-11-2023", 0],
    ["11-11-2023", 0],
    ...
  ]
}
```



### Rating History CSV
This Endpoint will generate CSV file of last 30 days rating of top 50 players

**Endpoint:** `/players/rating-history-csv`
```csv
username,09-11-2023,10-11-2023,11-11-2023,12-11-2023,13-11-2023,14-11-2023,15-11-2023,...
Apodex64,0,2532,2544,2544,2544,2544,2544,...
Unkreativ3,0,0,0,0,2522,2522,2522,...
Josip_buje,0,0,0,0,0,2533,2533,...
OjaiJoao,2479,2481,2481,2481,2481,2481,2481,...
igormezentsev,0,2472,2469,2469,2470,2476,2479,...
DrOrfeo,0,0,2429,2429,2429,2429,2429,...
```


