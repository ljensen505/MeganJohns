import { Button, Card } from "react-bootstrap";
import { Album } from "../types/Album";
import AlbumModal from "./AlbumModal";
import { useState } from "react";

interface AlbumCardProps {
  album: Album;
}

export default function AlbumCard(props: AlbumCardProps) {
  const album = props.album;

  const [show, setShow] = useState(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Card key={album.album_id} className="m-2">
        <Button variant="none" onClick={handleShow}>
          <Card.Img variant="top" src={album.front_artwork_url} />
          <Card.Body>
            <Card.Title>{album.album_name}</Card.Title>
            <Card.Subtitle>
              {album.artist.artist_name} ({album.release_year})
            </Card.Subtitle>
          </Card.Body>
        </Button>
      </Card>
      <AlbumModal album={album} show={show} onHide={() => setShow(false)} />
    </>
  );
}
