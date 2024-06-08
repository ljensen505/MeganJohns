interface BioParagraphContent {
  bioParagraph: string;
}

export default function BioP(props: BioParagraphContent) {
  return (
    <>
      <p>{props.bioParagraph}</p>
    </>
  );
}
