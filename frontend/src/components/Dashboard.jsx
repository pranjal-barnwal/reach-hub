import React, { useState, useEffect, useMemo } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const [topPlayers, setTopPlayers] = useState([]);
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [ratingHistory, setRatingHistory] = useState([]);
  const [chartData, setchartData] = useState([]);
  console.log(ratingHistory);
  useEffect(() => {
    // Fetch top players data from the FastAPI endpoint
    const fetchTopPlayers = async () => {
      try {
        const response = await axios.get("http://localhost:8000/top-players");
        setTopPlayers(response.data.top_players);
      } catch (error) {
        console.error("Error fetching top players:", error);
      }
    };

    fetchTopPlayers();
  }, []);

  // Fetch rating history when a player is selected
  useEffect(() => {
    const fetchRatingHistory = async () => {
      if (selectedPlayer) {
        try {
          const response = await axios.get(
            `http://localhost:8000/player/${selectedPlayer}/rating-history`
          );
          setRatingHistory(response.data.rating_history);
        } catch (error) {
          console.error(
            `Error fetching rating history for ${selectedPlayer}:`,
            error
          );
        }
      }
    };

    fetchRatingHistory();
  }, [selectedPlayer]);

  // Memoized chart data to prevent unnecessary re-renders
  useEffect(() => {
    const returndata = ratingHistory.length > 0 && ratingHistory.map((entry) => ({
      timestamp: entry.timestamp,
      rating: entry.rating,
    }));
    setchartData(returndata)
  }, [ratingHistory])

  return (
    <div>
      <h1>Chess Players Dashboard</h1>
      <div>
        <h2>Top Players</h2>
        <table>
          <thead>
            <tr>
              <th>Username</th>
              <th>Rating History</th>
            </tr>
          </thead>
          <tbody>
            {topPlayers.map((player) => (
              <tr key={player}>
                <td>{player[1]}</td>
                <td>
                  {/* Link to individual player's rating history */}
                  <Link to={`/player/${player[1]}`} target="_blank" rel="noopener noreferrer">
                    Graph Visualization
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {selectedPlayer && (
        <div>
          <h2>{selectedPlayer}'s Rating History</h2>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
