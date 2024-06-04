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

function App() {
  const [mj, setMj] = useState<MeganJohns | null>(null);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [artwork, setArtwork] = useState<Artwork[]>([]);

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
    }
  }, [mj]);

  return (
    <BrowserRouter>
      <Title />
      <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/music" element={<Discography albums={albums} />} />
        <Route path="/art" element={<Art allArtwork={artwork} />} />
      </Routes>
      {/* <Discography albums={albums} />
      <Art allArtwork={artwork} /> */}
    </BrowserRouter>
  );
}

export default App;
