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

function App() {
  const [mj, setMj] = useState<MeganJohns | undefined>(undefined);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [artwork, setArtwork] = useState<Artwork[]>([]);
  const [bio, setBio] = useState<Bio | undefined>(undefined);

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
      setAlbums(mj.albums);
      setArtwork(mj.artwork);
      setBio(mj.bio);
    }
  }, [mj]);

  if (!mj || !bio) {
    return <h4>Loading...</h4>;
  }

  return (
    <Container style={{ maxWidth: "1000px" }}>
      <Header mj={mj} />
      <About bio={bio} />
      <MjSection sectionTitle="discography" works={albums} />
      <MjSection sectionTitle="artwork" works={artwork} />
    </Container>
  );
}

export default App;
