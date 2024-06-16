import { Album } from "./types/Album";
import { Container } from "react-bootstrap";
import MjCarousel from "./MjCarousel/MjCarousel";
import { Artwork } from "./types/Artwork";

interface MjSectionProps {
  sectionTitle: string;
  works: Album[] | Artwork[];
}

export default function MjSection(props: MjSectionProps) {
  const sectionTitleAsTitle =
    props.sectionTitle.charAt(0).toUpperCase() + props.sectionTitle.slice(1);
  return (
    <section id={props.sectionTitle} className="content-section">
      <h2>{sectionTitleAsTitle}</h2>
      <Container>
        <MjCarousel works={props.works} />
      </Container>
    </section>
  );
}
