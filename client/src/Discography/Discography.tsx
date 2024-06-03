import { Album } from "../types/Album";
import { Container, Row } from "react-bootstrap";
import AlbumCard from "./AlbumCard";

interface DiscographyProps {
  albums: Album[];
}

export default function Discography(props: DiscographyProps) {
  return (
    <>
      <h2 id="discography">Discography</h2>
      <Container>
        <Row className="justify-content-center">
          {props.albums.map((album) => (
            <AlbumCard key={album.album_id} album={album} />
          ))}
        </Row>
      </Container>
    </>
  );
}
