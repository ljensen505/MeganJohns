import { Container } from "react-bootstrap";
import { Artwork } from "../types/Artwork";
import MjCarousel from "../MjCarousel/MjCarousel";

interface ArtworkProps {
  allArtwork: Artwork[];
}

export default function Art(props: ArtworkProps) {
  return (
    <>
      <h2 id="artwork">Artwork</h2>
      <Container fluid>
        <MjCarousel works={props.allArtwork} />
      </Container>
    </>
  );
}
