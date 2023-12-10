# Custom Lichess Backend with FastAPI & PostgreSQL
by **ReachHub** | [**Pranjal Kumar**](https://linkedin.com/in/pranjal-barnwal)

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
- [Top Player Data](#top-players-data)
- [Rating History for player](#rating-history-for-player)
- [Rating History CSV](#rating-history-csv)
---

### Top Players Data
This endpoint returns array of top players details. Each including: **[`id`,`username`,`rating`]**
> **Reference:** https://lichess.org/api/player/top/50/classical

**Endpoint:** `/top-players`

#### Sample Output
```json
{
  "top_players": [
    ["apodex64", "Apodex64", 2555],
    ["unkreativ3", "Unkreativ3", 2535],
    ["josip_buje", "Josip_buje", 2534],
    ...
  ]
}
```
---





### Rating History for player
This Endpoint will return last 30 dates ratings for the mentioned user. Each row including: **[`date`, `rating`]**
> **Reference:** https://lichess.org/api/user/{username}/rating-history/classical

For dates where no-rating is mentioned, we copied the last available data.

**Endpoint:** `/player/{username}/rating-history`

#### Sample Output
```json
{
  "points": [
    ["09-11-2023", 2102],
    ["10-11-2023", 2102],
    ["11-11-2023", 2350],
    ...
  ]
}
```
---



### Rating History CSV
This Endpoint will generate CSV file of last 30 days rating of top 50 players
It internally uses function call of Rating History of Player repetitively for Top 50 players following: ***Do not repeat principle***

**Endpoint:** `/players/rating-history-csv`

#### Sample Output
```csv
username,09-11-2023,10-11-2023,11-11-2023,12-11-2023,13-11-2023,14-11-2023,15-11-2023,...
Apodex64,0,2532,2544,2544,2544,2544,2544,...
Unkreativ3,0,0,0,0,2522,2522,2522,...
Josip_buje,0,0,0,0,0,2533,2533,...
OjaiJoao,2479,2481,2481,2481,2481,2481,2481,...
igormezentsev,0,2472,2469,2469,2470,2476,2479,...
DrOrfeo,0,0,2429,2429,2429,2429,2429,...
...
```
---


