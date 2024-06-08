import { Link } from "react-router-dom";

interface TitleProps {
  name?: string;
}

export default function Title(props: TitleProps) {
  return (
    <h1>
      <Link className="title" to="/">
        {props.name ? props.name : "Loading..."}
      </Link>
    </h1>
  );
}
