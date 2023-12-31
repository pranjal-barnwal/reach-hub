import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { saveAs } from 'file-saver';
import Loader from './Loader';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import { FiExternalLink } from "react-icons/fi";

const Dashboard = (props) => {
  const {topPlayers} = props;
  // const [topPlayers, setTopPlayers] = useState([]);
  // // console.log(ratingHistory);
  
  // useEffect(() => {
  //   // Fetch top players data from the FastAPI endpoint
  //   const fetchTopPlayers = async () => {
  //     try {
  //       const response = await axios.get("http://localhost:8000/top-players");
  //       setTopPlayers(response.data.top_players);
  //     } catch (error) {
  //       console.error("Error fetching top players:", error);
  //     }
  //   };

  //   fetchTopPlayers();

  //   // as soon the top players are loaded, we will check if rating history csv is loaded or not. If now, then we will start the process in background, so that when the person clicks the Download CSV button, it will appear to download faster
  // }, []);


  const downloadCSV = async () => {
    try {
      const response = await axios.get('http://localhost:8000/players/rating-history-csv', {
        responseType: 'blob', // Ensure the response type is set to blob
      });

      // Extract the file name from the response headers if available
      const contentDisposition = response.headers['content-disposition'];
      const fileNameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
      const matches = fileNameRegex.exec(contentDisposition);
      const filename = matches && matches[1] ? matches[1].replace(/['"]/g, '') : 'rating_history.csv';

      // Save the file using FileSaver.js
      saveAs(new Blob([response.data]), filename);
    } catch (error) {
      console.error("Error downloading CSV:", error);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", padding:"5% 30%"}}>
      <h1>Lichess Dashboard</h1>
      <div>
        <hr />
        <h2>Download</h2>
        <Button className="px-5 py-2" variant="success" title="Download 30 days History of Top 50 players in .csv format" onClick={downloadCSV} >
            Download CSV
        </Button>
        <hr />

        <h2>Top 50 Players</h2>
        {topPlayers.length > 0 ?

          <Table striped className="table-bordered table-hover">
            <thead>
              <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Rating</th>
                <th>Visualization</th>
              </tr>
            </thead>
            <tbody className="table-group-divider">
              {topPlayers.map((player) => (
                <tr key={player}>
                  <td>{player[0]}</td>
                  <td>{player[1]}</td>
                  <td>{player[2]}</td>
                  <td>
                    {/* Link to individual player's rating history */}
                    <Link className="link-success link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover fw-bold" to={`/player/${player[1]}`} rel="noopener noreferrer">
                      Graph <span className='customicon fw-bold'><FiExternalLink /></span>
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
          :
          <Loader/>
        }
      </div>
      
    </div>
  );
};

export default Dashboard;
