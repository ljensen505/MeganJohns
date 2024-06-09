import { MeganJohns } from "../types/MeganJohns";
import Title from "./Title";
import NavList from "./NavList";
import SocialBanner from "./SocialBanner/SocialBanner";

interface HeaderProps {
  mj?: MeganJohns;
}

export default function Header(props: HeaderProps) {
  if (!props.mj) {
    return <h4>Loading...</h4>;
  }
  const mj = props.mj;
  return (
    <>
      <SocialBanner socials={mj.bio.social_urls} />
      <Title name={mj.bio.name} />
      <NavList />
    </>
  );
}
