import { Button, Card } from "react-bootstrap";
import { Album } from "../types/Album";
import { Artwork } from "../types/Artwork";
import AlbumModal from "../Discography/AlbumModal";
import ArtworkModal from "../ArtworkSection/ArtworkModal";
import { useState } from "react";

interface CardProps {
  title: string;
  subtitle: string;
  work: Artwork | Album;
  img_src?: string;
}

export default function MjCard(props: CardProps) {
  const title = props.title;
  const subtitle = props.subtitle;
  const img_src = props.img_src;
  const work = props.work;
  const [show, setShow] = useState(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Card className="m-2">
        <Button variant="none" onClick={handleShow}>
          <Card.Img variant="top" src={img_src} />
          <Card.Body>
            <Card.Title>{title}</Card.Title>
            <Card.Subtitle>{subtitle}</Card.Subtitle>
          </Card.Body>
        </Button>
      </Card>
      {work instanceof Album ? (
        <AlbumModal
          album={work as Album}
          show={show}
          onHide={() => setShow(false)}
        />
      ) : (
        <ArtworkModal
          artwork={work as Artwork}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
    </>
  );
}
