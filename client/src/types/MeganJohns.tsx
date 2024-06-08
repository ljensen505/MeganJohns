import { Album } from "./Album";
import { Artwork } from "./Artwork";
import { Bio } from "./Bio";

class MeganJohns {
  albums: Album[];
  artwork: Artwork[];
  bio: Bio;

  constructor(albums: Album[], artwork: Artwork[], bio: Bio) {
    this.albums = albums;
    this.artwork = artwork;
    this.bio = bio;
  }
}

export { MeganJohns };
