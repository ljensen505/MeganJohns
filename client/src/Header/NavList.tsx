import { ListGroup } from "react-bootstrap";
import "./Header.css";

export default function NavList() {
  return (
    <ListGroup horizontal className="justify-content-center mb-4">
      <ListGroup.Item>
        <a href="#root">About</a>
      </ListGroup.Item>
      <ListGroup.Item>
        <a href="#discography">Music</a>
      </ListGroup.Item>
      <ListGroup.Item>
        <a href="#artwork">Art</a>
      </ListGroup.Item>
      <ListGroup.Item disabled>News</ListGroup.Item>
    </ListGroup>
  );
}
