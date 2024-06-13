interface TitleProps {
  name: string;
}

export default function Title(props: TitleProps) {
  return (
    <h2>
      {/* <Link className="title" to="/">
        {props.name}
      </Link> */}
      <a href="#root" className="title" id="title">
        {props.name}
      </a>
    </h2>
  );
}
