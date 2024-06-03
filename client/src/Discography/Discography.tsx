import { Album } from "../types/Album";
import { ListGroup } from "react-bootstrap";

interface DiscographyProps {
  albums: Album[];
}

export default function Discography(props: DiscographyProps) {
  return (
    <>
      <h3>Discography</h3>
      <ListGroup>
        {props.albums.map((album) => (
          <ListGroup.Item key={album.album_id}>
            {album.album_name} ({album.release_year})
          </ListGroup.Item>
        ))}
      </ListGroup>
    </>
  );
}
