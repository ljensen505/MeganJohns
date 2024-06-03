class Medium {
  medium_id: number;
  medium_name: string;

  constructor(medium_id: number, medium_name: string) {
    this.medium_id = medium_id;
    this.medium_name = medium_name;
  }
}

class Artwork {
  artwork_id: number;
  artwork_name: string;
  medium: Medium;
  source_url: string;
  release_year: string;
  size?: string;

  constructor(
    artwork_id: number,
    artwork_name: string,
    medium: Medium,
    source_url: string,
    release_year: string,
    size?: string
  ) {
    this.artwork_id = artwork_id;
    this.artwork_name = artwork_name;
    this.medium = medium;
    this.source_url = source_url;
    this.release_year = release_year;
    this.size = size;
  }
}

export { Medium, Artwork };
