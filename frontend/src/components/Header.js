import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';

const navbarStyle = {
  backgroundColor: '#eeeeee',
};

const Header = ({ title, clearPage }) => {
  return (
    <Navbar style={navbarStyle} variant="light">
      <Nav.Link onClick={clearPage}>
        <Container>
          <Logo alt={title} style={{ maxWidth: '12rem', maxHeight: '3rem' }} />
        </Container>
      </Nav.Link>
    </Navbar>
  );
};

export default Header;
