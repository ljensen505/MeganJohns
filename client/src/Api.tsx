import axios from "axios";
import { MeganJohns } from "./types/MeganJohns";
import { Album } from "./types/Album";
import { Artwork } from "./types/Artwork";

const baseURL = import.meta.env.VITE_API_URL as string;

const api = axios.create({ baseURL: baseURL });

export const getMeganJohns = async (): Promise<MeganJohns> => {
  const response = await api.get<MeganJohns>("/");
  const albums = response.data.albums.map(constructAlbum);
  const artwork = response.data.artwork.map(constructArtwork);
  return new MeganJohns(albums, artwork, response.data.bio);
};

function constructAlbum(data: Album): Album {
  return new Album(
    data.album_id,
    data.album_name,
    data.release_year,
    data.artist,
    data.spotify_url,
    data.itunes_url,
    data.bandcamp_url,
    data.apple_music_url,
    data.front_artwork_url,
    data.rear_artwork_url,
    data.bandcamp_player
  );
}

function constructArtwork(data: Artwork): Artwork {
  return new Artwork(
    data.artwork_id,
    data.artwork_name,
    data.medium,
    data.source_url,
    data.release_year,
    data.size
  );
}
