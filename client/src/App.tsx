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
import Title from "./Header/Title";
import { Bio } from "./types/Bio";

function App() {
  const [mj, setMj] = useState<MeganJohns | null>(null);
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

  return (
    <BrowserRouter>
      <Title name={mj?.bio.name} />
      <Header />
      <Routes>
        <Route path="/" element={<Homepage bio={bio} />} />
        <Route path="/music" element={<Discography albums={albums} />} />
        <Route path="/art" element={<Art allArtwork={artwork} />} />
      </Routes>
      {/* <Discography albums={albums} />
      <Art allArtwork={artwork} /> */}
    </BrowserRouter>
  );
}

export default App;
