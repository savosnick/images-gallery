import React from 'react';
import { Card, Button, Nav } from 'react-bootstrap';

const Author = (image) => {
  if (image.user?.portfolio_url)
    return (
      <Nav.Link href={image.user.portfolio_url} target="_blank">
        {image.user.name}
      </Nav.Link>
    );
  else if (image.user?.name) return image.user.name;
  else return 'No author name';
};

const ImageCard = ({ image, deleteImage, saveImage }) => {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image.urls.small} />
      <Card.Body>
        <Card.Title>
          {image.title?.[0].toUpperCase() + image.title?.slice(1)}
        </Card.Title>
        <Card.Text>{image.description || image.alt_description}</Card.Text>
        <Button variant="primary" onClick={() => deleteImage(image.id)}>
          Delete
        </Button>{' '}
        {!image.saved && (
          <Button variant="secondary" onClick={() => saveImage(image.id)}>
            Save
          </Button>
        )}
      </Card.Body>
      <Card.Footer className="text-center text-muted">
        {Author(image)}
      </Card.Footer>
    </Card>
  );
};

export default ImageCard;
