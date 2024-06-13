import { ListGroup } from "react-bootstrap";

export default function NavList() {
  return (
    <ListGroup horizontal className="justify-content-center mb-4">
      <ListGroup.Item>
        {/* <Link to="/">About</Link> */}
        <a href="#root">About</a>
      </ListGroup.Item>
      <ListGroup.Item>
        {/* <Link to="/music">Music</Link> */}
        <a href="#discography">Music</a>
      </ListGroup.Item>
      <ListGroup.Item>
        {/* <Link to="/art">Art</Link> */}
        <a href="#artwork">Art</a>
      </ListGroup.Item>
      <ListGroup.Item disabled>News</ListGroup.Item>
    </ListGroup>
  );
}
