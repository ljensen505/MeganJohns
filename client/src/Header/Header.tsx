import ListGroup from "react-bootstrap/ListGroup";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <ListGroup horizontal className="justify-content-center mb-4">
      <ListGroup.Item>
        <Link to="/music">Music</Link>
      </ListGroup.Item>
      <ListGroup.Item>
        <Link to="/art">Art</Link>
      </ListGroup.Item>
      <ListGroup.Item>News</ListGroup.Item>
    </ListGroup>
  );
}
