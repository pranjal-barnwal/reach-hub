import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import RatingHistory from "./components/RatingHistory";
import Header from "./components/Header";
import Footer from "./components/Footer";


export default function App() {
 
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/player/:player" element={<RatingHistory/>} />

        </Routes>
      <Footer />
    </BrowserRouter>
  );
}