import axios from "axios";
import { MeganJohns } from "./types/MeganJohns";
import { Album } from "./types/Album";
import { Artwork } from "./types/Artwork";
import { Quote } from "./types/Quote";
import { Video } from "./types/Video";
import { Bio } from "./types/Bio";

const baseURL = import.meta.env.VITE_API_URL as string;

const api = axios.create({ baseURL: baseURL });

export const getMeganJohns = async (): Promise<MeganJohns> => {
  const response = await api.get<MeganJohns>("/");
  const albums = response.data.albums.map(constructAlbum);
  const artwork = response.data.artwork.map(constructArtwork);
  const quotes = response.data.quotes.map(constructQuote);
  const videos = response.data.videos.map(constructVideo);
  const bio = constructBio(response.data.bio);
  return new MeganJohns(albums, artwork, quotes, videos, bio);
};

function constructBio(data: Bio): Bio {
  return new Bio(data.name, data.bio, data.social_urls);
}

function constructVideo(data: Video): Video {
  return new Video(
    data.id,
    data.title,
    data.subtitle,
    data.description,
    data.youtube_player
  );
}

function constructQuote(data: Quote): Quote {
  return new Quote(data.id, data.body, data.author, data.source);
}

function constructAlbum(data: Album): Album {
  return new Album(
    data.id,
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
    data.id,
    data.artwork_name,
    data.medium,
    data.source_url,
    data.release_year,
    data.size
  );
}
