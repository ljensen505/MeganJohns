import { Album } from "./Album";
import { Artwork } from "./Artwork";

class MeganJohns {
  albums: Album[];
  artwork: Artwork[];

  constructor(albums: Album[], artwork: Artwork[]) {
    this.albums = albums;
    this.artwork = artwork;
  }
}

export { MeganJohns };
