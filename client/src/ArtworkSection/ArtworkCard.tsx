import { Button, Card } from "react-bootstrap";
import { Artwork } from "../types/Artwork";
import { useState } from "react";
import ArtworkModal from "./ArtworkModal";

interface ArtworkCardProps {
  artwork: Artwork;
}

export default function ArtworkCard(props: ArtworkCardProps) {
  const artwork = props.artwork;
  const [modalShow, setModalShow] = useState(false);
  return (
    <>
      <Card className="m-2">
        <Button variant="none" onClick={() => setModalShow(true)}>
          <Card.Img variant="top" src={props.artwork.source_url} />
          <Card.Body>
            <Card.Title>{artwork.artwork_name}</Card.Title>
            <Card.Subtitle>
              {artwork.medium.medium_name} {artwork.size} (
              {artwork.release_year})
            </Card.Subtitle>
          </Card.Body>
        </Button>
      </Card>
      <ArtworkModal
        show={modalShow}
        onHide={() => setModalShow(false)}
        artwork={artwork}
      />
    </>
  );
}
