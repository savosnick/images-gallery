import React from 'react';
import { Spinner as Loader } from 'react-bootstrap';

const Spinner = () => {
  return (
    <Loader
      style={{
        position: 'fixed',
        top: '50%',
        left: '50%',
      }}
      animation="border"
    />
  );
};

export default Spinner;
