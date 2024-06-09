import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { SocialUrl } from "../../types/Bio";
import {
  faItunesNote,
  faFacebook,
  faSoundcloud,
  faYoutube,
  faInstagram,
  faSpotify,
  IconDefinition,
} from "@fortawesome/free-brands-svg-icons";
import { Container, ListGroup } from "react-bootstrap";
import "./SocialBanner.css";

interface SocialBannerProps {
  socials: SocialUrl[];
}

export default function SocialBanner(props: SocialBannerProps) {
  const socials = props.socials;
  const socialIconMap: { [key: string]: IconDefinition } = {
    itunes: faItunesNote,
    facebook: faFacebook,
    soundcloud: faSoundcloud,
    youtube: faYoutube,
    instagram: faInstagram,
    spotify: faSpotify,
  };

  return (
    <Container>
      <ListGroup horizontal className="justify-content-center">
        {socials.map((social) => (
          <ListGroup.Item key={social.social_id} className="social-icon">
            <a href={social.social_url}>
              <FontAwesomeIcon
                icon={socialIconMap[social.social_name]}
                className="social-icon"
              />
            </a>
          </ListGroup.Item>
        ))}
      </ListGroup>
    </Container>
  );
}