import { useEffect, useState } from "react";
import { getMeganJohns } from "./Api";
import "./App.css";
import { MeganJohns } from "./types/MeganJohns";
import { Album } from "./types/Album";
import { Artwork } from "./types/Artwork";
import MjSection from "./MjSection";
import Header from "./Header/Header";
import About from "./About/Homepage";
import { Bio } from "./types/Bio";
import { Container } from "react-bootstrap";
import { Quote } from "./types/Quote";
import Quotes from "./Quotes/Quotes";
import { Video } from "./types/Video";

function App() {
  const [mj, setMj] = useState<MeganJohns | undefined>(undefined);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [artwork, setArtwork] = useState<Artwork[]>([]);
  const [bio, setBio] = useState<Bio | undefined>(undefined);
  const [quotes, setQuotes] = useState<Quote[]>([]);
  const [videos, setVideos] = useState<Video[]>([]);

  useEffect(() => {
    getMeganJohns().then(
      (mjData) => {
        setMj(mjData);
      },
      (error) => {
        console.error(error);
      }
    );
  }, []);

  useEffect(() => {
    if (mj) {
      console.log(mj);
      setAlbums(mj.albums);
      setArtwork(mj.artwork);
      setBio(mj.bio);
      setQuotes(mj.quotes);
      setVideos(mj.videos);
    }
  }, [mj]);

  if (!mj || !bio) {
    return <></>;
  }

  return (
    <Container style={{ maxWidth: "1000px" }}>
      <Header mj={mj} />
      <About bio={bio} />
      <MjSection sectionTitle="discography" works={albums} />
      <MjSection sectionTitle="artwork" works={artwork} />
      <MjSection sectionTitle="videos" works={videos} />
      <Quotes quotes={quotes} />
    </Container>
  );
}

export default App;
