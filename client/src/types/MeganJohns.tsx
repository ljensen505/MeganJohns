import { Album } from "./Album";
import { Artwork } from "./Artwork";
import { Bio } from "./Bio";
import { Quote } from "./Quote";
import { Video } from "./Video";

class MeganJohns {
  albums: Album[];
  artwork: Artwork[];
  quotes: Quote[];
  videos: Video[];
  bio: Bio;

  constructor(
    albums: Album[],
    artwork: Artwork[],
    quotes: Quote[],
    videos: Video[],
    bio: Bio
  ) {
    this.albums = albums;
    this.artwork = artwork;
    this.quotes = quotes;
    this.videos = videos;
    this.bio = bio;
  }
}

export { MeganJohns };
