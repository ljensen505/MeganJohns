import { Bio } from "../types/Bio";
import BioComp from "./BioComp";

interface HomepageProps {
  bio: Bio;
}

export default function Homepage(props: HomepageProps) {
  const bio = props.bio;

  return (
    <>
      <BioComp bioContent={bio.bio} />
    </>
  );
}
