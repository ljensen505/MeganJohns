import { Bio } from "../types/Bio";
import BioComp from "./BioComp";

interface HomepageProps {
  bio?: Bio;
}

export default function Homepage(props: HomepageProps) {
  const bio = props.bio;
  if (!bio) {
    return <h4>Loading...</h4>;
  }
  return (
    <>
      <BioComp bioContent={bio.bio} />
    </>
  );
}
