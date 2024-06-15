import { Container } from "react-bootstrap";
import { Bio } from "../types/Bio";

interface HomepageProps {
  bio: Bio;
}

export default function Homepage(props: HomepageProps) {
  const bio = props.bio;
  const bioHTML = () => {
    return { __html: bio.bio };
  };

  return (
    <>
      {/* <div dangerouslySetInnerHTML={bioHTML()} /> */}
      <Container id="home">
        <div dangerouslySetInnerHTML={bioHTML()} />
      </Container>
    </>
  );
}
