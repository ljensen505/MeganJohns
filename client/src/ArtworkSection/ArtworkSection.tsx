import { Container, Row } from "react-bootstrap";
import { Artwork } from "../types/Artwork";
import ArtworkCard from "./ArtworkCard";

interface ArtworkProps {
  allArtwork: Artwork[];
}

export default function Art(props: ArtworkProps) {
  if (props.allArtwork.length > 0) {
    console.log(props.allArtwork);
  }
  return (
    <>
      <h2>Artwork</h2>
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
