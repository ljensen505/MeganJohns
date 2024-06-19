import { Container, Modal } from "react-bootstrap";
import { Video } from "../types/Video";
import "./VideoModal.css";

interface VideoModalProps {
  video: Video;
  show: boolean;
  onHide: () => void;
}

export default function VideoModal(props: VideoModalProps) {
  const video = props.video;
  const youtubePlayer = video.youtube_player ? (
    <div
      dangerouslySetInnerHTML={{
        __html: video.youtube_player,
      }}
    />
  ) : null;

  const handleClose = () => {
    props.onHide();
  };

  return (
    <Modal {...props} onHide={handleClose} size="lg" centered>
      <Modal.Header closeButton>
        <Modal.Title id={`{video.title}-modal`}>{video.title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>{video.title}</p>
        <p>{video.subtitle}</p>
        <Container className="youtube-player-container">
          {youtubePlayer}
        </Container>
      </Modal.Body>
      <Modal.Footer>
        <p>{video.description}</p>
      </Modal.Footer>
    </Modal>
  );
}
