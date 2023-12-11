import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import RatingHistory from "./components/RatingHistory";
import Header from "./components/Header";
import Footer from "./components/Footer";
import axios from "axios";


export default function App() {
  const [topPlayers, setTopPlayers] = useState([]);
  // console.log(ratingHistory);
  
  useEffect(() => {
    // Fetch top players data from the FastAPI endpoint
    const fetchTopPlayers = async () => {
      try {
        const response = await axios.get("http://localhost:8000/top-players");
        setTopPlayers(response.data.top_players);
        console.log(topPlayers);
      } catch (error) {
        console.error("Error fetching top players:", error);
      }
    };

    fetchTopPlayers();

    // as soon the top players are loaded, we will check if rating history csv is loaded or not. If now, then we will start the process in background, so that when the person clicks the Download CSV button, it will appear to download faster
  }, []);
  
 
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard topPlayers={topPlayers}/>} />
        <Route path="/player/:player" element={<RatingHistory/>} />

        </Routes>
      <Footer />
    </BrowserRouter>
  );
}