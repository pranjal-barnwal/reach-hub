import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import Loader from "./Loader";
import Button from 'react-bootstrap/Button';

function RatingHistory() {
  const { player } = useParams();
  const [ratingHistory, setRatingHistory] = useState([]);
  const [data, setdata] = useState([]);

  useEffect(() => {
    console.log(player);
    const rating = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/player/${player}/rating-history`
        );
        let rating_history_arr = response?.data?.points
        let rating_history = rating_history_arr.map((item) => {
          return {
            date: item[0],
            rating: item[1]
          };
        });
        console.log(rating_history);
        setRatingHistory(rating_history);
        setdata(rating_history)
      } catch (error) {
        console.error("Error fetching top players:", error);
      }
    };
    rating();
  }, []);

  const redirectToOfficial = () => {
    let url = 'https://lichess.org/@/' + player;
    window.open(url, '_blank');
  }


  return (
    <div style={{ width: "100%", height: "100vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
      {data.length > 0 ?
        <>
          <h1>Last 30 days of {player}'s Data</h1>
          <ResponsiveContainer width="50%" height="60%">
            <LineChart
              width={500}
              height={300}
              data={ratingHistory}
              margin={{
                top: 55,
                right: 30,
                left: 30,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" padding={{ left: 10, right: 10 }} />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line
                type="monotone"
                dataKey="rating"
                stroke="#82ca9d"
                activeDot={{ r: 8 }}
              />
            </LineChart>
          </ResponsiveContainer>
          <Button className="mt-3 px-5 py-2" variant="secondary" title="View the profile on Official Lichess Portal" onClick={redirectToOfficial} >
            {player}'s profile
          </Button>
        </>
        :
        <Loader />}

    </div>
  );
}

export default RatingHistory;
