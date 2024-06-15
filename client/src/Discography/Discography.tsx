import { Album } from "../types/Album";
import { Container } from "react-bootstrap";
import MjCarousel from "../MjCarousel/MjCarousel";

interface DiscographyProps {
  albums: Album[];
}

export default function Discography(props: DiscographyProps) {
  console.log(props.albums);
  return (
    <>
      <h2 id="discography">Discography</h2>
      <Container>
        <MjCarousel works={props.albums} />
      </Container>
    </>
  );
}
