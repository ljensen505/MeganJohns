import { BioParagraph } from "../types/Bio";
import BioP from "./BioP";

interface BioCompProps {
  bioContent: BioParagraph[];
}

export default function BioComp(props: BioCompProps) {
  return (
    <>
      {props.bioContent.map((bioParagraph) => (
        <BioP
          key={bioParagraph.bio_paragraph_id}
          bioParagraph={bioParagraph.bio_paragraph}
        />
      ))}
    </>
  );
}
