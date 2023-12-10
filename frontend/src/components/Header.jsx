import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


const Header = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const navigate = useNavigate();

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevents the default form submission behavior
      redirectToProfile();
    }
    setSearchTerm(event.target.value);
  };
  
  const redirectToProfile = () => {
    navigate(`/player/${searchTerm}`);
  };

  return (
    <Navbar bg="dark" data-bs-theme="dark" expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="/" className='font-weight-bold'>Lichess Portal</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/">Dashboard</Nav.Link>
            <Nav.Link href="https://github.com/pranjal-barnwal/reach-hub">Repo</Nav.Link>
            <Nav.Link href="https://reachhub.co">ReachHub</Nav.Link>
          </Nav>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search username"
              className="me-2"
              aria-label="Search"
              onChange={(e) => handleKeyPress(e)}
            />
            <Button variant="success" onClick={redirectToProfile}>Go</Button>
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}

export default Header