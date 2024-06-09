import { useEffect, useState } from "react";
import { getMeganJohns } from "./Api";
import "./App.css";
import { MeganJohns } from "./types/MeganJohns";
import { Album } from "./types/Album";
import { Artwork } from "./types/Artwork";
import Discography from "./Discography/Discography";
import Art from "./ArtworkSection/ArtworkSection";
import Header from "./Header/Header";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Homepage from "./Homepage/Homepage";
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
      console.log(mj);
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
      <BrowserRouter>
        <Header mj={mj} />
        <Routes>
          <Route path="/" element={<Homepage bio={bio} />} />
          <Route path="/music" element={<Discography albums={albums} />} />
          <Route path="/art" element={<Art allArtwork={artwork} />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}

export default App;
