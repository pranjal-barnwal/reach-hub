import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

function RatingHistory() {
  const { player } = useParams();
  const [ratingHistory, setRatingHistory] = useState([]);
  const [Chessname, setname] = useState([]);
  const [dates, setdates] = useState([]);
  const [data, setdata] = useState([]);

  useEffect(() => {
    console.log(player);
    const rating = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/player/${player}/rating-history`
        );
        let rating_history = response?.data?.points
        rating_history = rating_history.map((item) => item[1]);
        console.log(rating_history);
        setRatingHistory(rating_history);
      } catch (error) {
        console.error("Error fetching top players:", error);
      }
    };
    rating();
  }, []);

  function formatLast20Dates(dateArrays) {
    // Ensure there are at least 20 elements
    const last20Dates = dateArrays.slice(-20);

    return last20Dates.map((dateArray) => {
      const year = dateArray[0];
      const month = dateArray[1];
      const day = dateArray[2];
      const date = new Date(year, month - 1, day);
      const dd = String(date.getDate()).padStart(2, "0");
      const mm = String(date.getMonth() + 1).padStart(2, "0");
      const yy = String(date.getFullYear()).slice(-2);
      return `${dd}/${mm}/${yy}`;
    });
  }

  useEffect(() => {
    const dates = Chessname?.length > 0 && formatLast20Dates(Chessname);
    setdates(dates)
  }, [Chessname]);

  useEffect(() => {
    // const data = Chessname?.length > 0 && formatLast20Dates(Chessname);
    // setdata(data)
    const arrayOfObjects = [];

    // Loop through the arrays and create objects
    for (let i = 0; i < dates.length; i++) {
      const obj = {
        date: dates[i],
        rating: Chessname[i][3]

      };

      arrayOfObjects.push(obj);
    }
    setdata(arrayOfObjects)

  }, [dates]);




  return (
    <div style={{ width: "100%", height: "100vh", display: "flex", justifyContent: "center", alignItems: "center" }}>
      {data.length > 0 ? <ResponsiveContainer width="50%" height="50%">
        <LineChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="rating"
            stroke="#8884d8"
            activeDot={{ r: 8 }}
          />
        </LineChart>
      </ResponsiveContainer> : <div>
        No Data</div>}

    </div>
  );
}

export default RatingHistory;
