import { Carousel } from "react-bootstrap";
import { Album } from "../types/Album";
import { Container, Row } from "react-bootstrap";
import MjCard from "./MjCard";
import { Artwork } from "../types/Artwork";

interface CarouselProps {
  works: Album[] | Artwork[];
}

export default function MjCarousel(props: CarouselProps) {
  const works = props.works;
  return (
    <>
      <Container
        id={
          works[0] instanceof Album
            ? "discography-carousel"
            : "artwork-carousel"
        }
      >
        <Carousel>
          {works.map((work) => (
            <Carousel.Item
              key={work instanceof Album ? work.album_id : work.artwork_id}
              className="justify-content-center"
            >
              <Container>
                <Row className="justify-content-center">
                  <MjCard
                    title={
                      work instanceof Album
                        ? work.album_name
                        : work.artwork_name
                    }
                    subtitle={
                      work instanceof Album
                        ? `${(work as Album).artist.artist_name} (${
                            (work as Album).release_year
                          })`
                        : ""
                    }
                    work={work}
                    img_src={
                      work instanceof Album
                        ? (work as Album).front_artwork_url
                        : (work as Artwork).source_url
                    }
                  />
                </Row>
              </Container>
            </Carousel.Item>
          ))}
        </Carousel>
      </Container>
    </>
  );
}
