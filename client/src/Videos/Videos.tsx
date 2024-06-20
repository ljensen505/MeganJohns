import { Container, ListGroup, Row } from "react-bootstrap";
import { Video } from "../types/Video";

interface VideosProps {
  videos: Video[];
}

export default function Videos(props: VideosProps) {
  const videos = props.videos;

  return (
    <section id="videos" className="content-section">
      <h2>Videos</h2>
      <Container>
        <Row>
          <ListGroup>
            {videos.map((video) => (
              <ListGroup.Item key={video.id} className="">
                <Container className="youtube-player-container">
                  <div
                    dangerouslySetInnerHTML={{
                      __html: video.youtube_player,
                    }}
                  />
                </Container>
              </ListGroup.Item>
            ))}
          </ListGroup>
        </Row>
      </Container>
    </section>
  );
}
