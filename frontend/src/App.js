import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import RatingHistory from "./components/RatingHistory";


export default function App() {
 
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/player/:player" element={<RatingHistory/>} />

        </Routes>
    </BrowserRouter>
  );
}