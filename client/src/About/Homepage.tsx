import { Container } from "react-bootstrap";
import { Bio } from "../types/Bio";

interface AboutProps {
  bio: Bio;
}

export default function About(props: AboutProps) {
  const bio = props.bio;
  const bioHTML = () => {
    return { __html: bio.bio };
  };

  return (
    <Container id="home" className="content-section">
      <div dangerouslySetInnerHTML={bioHTML()} />
    </Container>
  );
}
