import { Album } from "./Album";
import { Artwork } from "./Artwork";
import { Bio } from "./Bio";
import { Quote } from "./Quote";

class MeganJohns {
  albums: Album[];
  artwork: Artwork[];
  quotes: Quote[];
  bio: Bio;

  constructor(albums: Album[], artwork: Artwork[], quotes: Quote[], bio: Bio) {
    this.albums = albums;
    this.artwork = artwork;
    this.quotes = quotes;
    this.bio = bio;
  }
}

export { MeganJohns };
