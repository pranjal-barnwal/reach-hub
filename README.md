# Reach Hub
Assignment files for reach-hub

# Player names for testing

- Apodex64
- sahibsinghknight
- Unkreativ3
- Josip_buje

# Sample Data

## Top Players Data

> https://lichess.org/api/player/top/50/classical

```json
{
  "users": [
    {
      "id": "apodex64",
      "username": "Apodex64",
      "perfs": {
        "classical": {
          "rating": 2555,
          "progress": 56
        }
      }
    },
    {
      "id": "unkreativ3",
      "username": "Unkreativ3",
      "perfs": {
        "classical": {
          "rating": 2535,
          "progress": 32
        }
      },
      "title": "FM",
      "online": true
    }
  ]
}
```

`Only showing 2 users instead of 50 for simplicity`



## Rating History for player
> https://lichess.org/api/user/{username}/rating-history/classical
```json
[
  {
    "name": "Bullet",
    "points": []
  },
  {
    "name": "Blitz",
    "points": []
  },
  {
    "name": "Rapid",
    "points": []
  },
  {
    "name": "Classical",
    "points": []
  },
  {
    "name": "Correspondence",
    "points": []
  },
  {
    "name": "Chess960",
    "points": []
  },
  {
    "name": "King of the Hill",
    "points": []
  },
  {
    "name": "Three-check",
    "points": []
  },
  {
    "name": "Antichess",
    "points": []
  },
  {
    "name": "Atomic",
    "points": []
  },
  {
    "name": "Horde",
    "points": []
  },
  {
    "name": "Racing Kings",
    "points": []
  },
  {
    "name": "Crazyhouse",
    "points": []
  },
  {
    "name": "Puzzles",
    "points": []
  },
  {
    "name": "UltraBullet",
    "points": []
  }
]
```
