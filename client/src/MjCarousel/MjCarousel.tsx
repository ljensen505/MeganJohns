import { Carousel } from "react-bootstrap";
import { Album } from "../types/Album";
import { Container, Row } from "react-bootstrap";
import MjCard from "./MjCard";
import { Artwork } from "../types/Artwork";
import { Video } from "../types/Video";

interface CarouselProps {
  works: Album[] | Artwork[] | Video[];
}

export default function MjCarousel(props: CarouselProps) {
  const works = props.works;
  return (
    <>
      <Container id={`${works[0].type}-carousel`}>
        <Carousel>
          {works.map((work) => (
            <Carousel.Item
              key={`${work.type}-${work.id}`}
              className="justify-content-center"
            >
              <Container>
                <Row className="justify-content-center">
                  <MjCard work={work} />
                </Row>
              </Container>
            </Carousel.Item>
          ))}
        </Carousel>
      </Container>
    </>
  );
}
