import { Link } from "react-router-dom";

interface TitleProps {
  name: string;
}

export default function Title(props: TitleProps) {
  return (
    <h2>
      <Link className="title" to="/">
        {props.name}
      </Link>
    </h2>
  );
}
