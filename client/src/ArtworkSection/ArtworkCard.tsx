import { Card } from "react-bootstrap";
import { Artwork } from "../types/Artwork";

interface ArtworkCardProps {
  artwork: Artwork;
}

export default function ArtworkCard(props: ArtworkCardProps) {
  const artwork = props.artwork;
  return (
    <Card className="m-2">
      <Card.Img variant="top" src={props.artwork.source_url} />
      <Card.Body>
        <Card.Title>{artwork.artwork_name}</Card.Title>
        <Card.Subtitle>
          {artwork.medium.medium_name} {artwork.size} ({artwork.release_year})
        </Card.Subtitle>
      </Card.Body>
    </Card>
  );
}
