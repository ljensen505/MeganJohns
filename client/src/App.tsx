import { useEffect, useState } from "react";
import { getMeganJohns } from "./Api";
import "./App.css";
import { MeganJohns } from "./types/MeganJohns";
import { Album } from "./types/Album";
import { Artwork } from "./types/Artwork";
import Discography from "./Discography/Discography";
import Art from "./ArtworkSection/ArtworkSection";

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
    <>
      <h1>Megan Johns</h1>
      <Discography albums={albums} />
      <Art allArtwork={artwork} />
    </>
  );
}

export default App;
