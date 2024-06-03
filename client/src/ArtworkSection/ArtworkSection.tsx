import { Container, Row } from "react-bootstrap";
import { Artwork } from "../types/Artwork";
import ArtworkCard from "./ArtworkCard";

interface ArtworkProps {
  allArtwork: Artwork[];
}

export default function Art(props: ArtworkProps) {
  return (
    <>
      <h2 id="artwork">Artwork</h2>
      <Container fluid>
        <Row className="justify-content-center">
          {props.allArtwork.map((artwork) => (
            <ArtworkCard key={artwork.artwork_id} artwork={artwork} />
          ))}
        </Row>
      </Container>
    </>
  );
}
