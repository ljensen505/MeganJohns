import { Button, Card } from "react-bootstrap";
import { Album } from "../types/Album";
import AlbumModal from "./AlbumModal";
import { useState } from "react";

interface AlbumCardProps {
  album: Album;
}

export default function AlbumCard(props: AlbumCardProps) {
  const [modalShow, setModalShow] = useState<boolean>(false);
  const album = props.album;

  return (
    <Card
      key={album.album_id}
      style={{
        width: "18rem",
      }}
    >
      <Button variant="none" onClick={() => setModalShow(true)}>
        <AlbumModal
          album={album}
          show={modalShow}
          onHide={() => setModalShow(false)}
        />
        <Card.Img variant="top" src={album.front_artwork_url} />
        <Card.Body>
          <Card.Title>{album.album_name}</Card.Title>
          <Card.Subtitle>
            {album.artist.artist_name} ({album.release_year})
          </Card.Subtitle>
        </Card.Body>
      </Button>
    </Card>
  );
}
