import { Button, Card } from "react-bootstrap";
import { Album } from "../types/Album";
import { Artwork } from "../types/Artwork";
import AlbumModal from "../Discography/AlbumModal";
import ArtworkModal from "../ArtworkSection/ArtworkModal";
import { useState } from "react";
import { Video } from "../types/Video";
import VideoModal from "../Videos/VideoModal";

interface CardProps {
  work: Artwork | Album | Video;
}

export default function MjCard(props: CardProps) {
  const work = props.work;
  let title: string;
  let img_src: string | undefined;
  let subtitle: string;
  let album: Album;
  let artwork: Artwork;
  let video: Video;
  switch (work.type) {
    case "album":
      album = work as Album;
      title = album.album_name;
      subtitle = `${album.artist.artist_name} (${album.release_year})`;
      img_src = (work as Album).front_artwork_url;
      break;
    case "artwork":
      artwork = work as Artwork;
      title = artwork.artwork_name;
      subtitle = `${artwork.medium.medium_name} (${artwork.release_year})`;
      img_src = artwork.source_url;
      break;
    case "video":
      video = work as Video;
      title = video.title;
      subtitle = video.subtitle;
      img_src = video.youtube_player;
      break;
    default:
      title = "";
      subtitle = "";
      img_src = "";
      break;
  }

  const [show, setShow] = useState(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Card className="m-3">
        <Button variant="none" onClick={handleShow}>
          {img_src && <Card.Img variant="top" src={img_src} />}
          <Card.Body>
            <Card.Title>{title}</Card.Title>
            <Card.Subtitle>{subtitle}</Card.Subtitle>
          </Card.Body>
        </Button>
      </Card>
      {work.type === "album" && (
        <AlbumModal
          album={work as Album}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
      {work.type === "artwork" && (
        <ArtworkModal
          artwork={work as Artwork}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
      {work.type == "video" && (
        <VideoModal
          video={work as Video}
          show={show}
          onHide={() => setShow(false)}
        />
      )}
    </>
  );
}
