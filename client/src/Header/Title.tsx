import { Link } from "react-router-dom";

export default function Title() {
  return (
    <h1>
      <Link className="title" to="/">
        Megan Johns
      </Link>
    </h1>
  );
}
