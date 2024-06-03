class Artist {
  artist_id: number;
  artist_name: string;
  artist_url?: string;

  constructor(artist_id: number, artist_name: string, artist_url?: string) {
    this.artist_id = artist_id;
    this.artist_name = artist_name;
    this.artist_url = artist_url;
  }
}

class Album {
  album_id: number;
  album_name: string;
  release_year: number;
  artist: Artist;
  spotify_url?: string;
  itunes_url?: string;
  bandcamp_url?: string;
  apple_music_url?: string;
  front_artwork_url?: string;
  rear_artwork_url?: string;
  bandcamp_player?: string;

  constructor(
    album_id: number,
    album_name: string,
    release_year: number,
    artist: Artist,
    spotify_url?: string,
    itunes_url?: string,
    bandcamp_url?: string,
    apple_music_url?: string,
    front_artwork_url?: string,
    rear_artwork_url?: string,
    bandcamp_player_src?: string
  ) {
    this.album_id = album_id;
    this.album_name = album_name;
    this.release_year = release_year;
    this.artist = artist;
    this.spotify_url = spotify_url;
    this.itunes_url = itunes_url;
    this.bandcamp_url = bandcamp_url;
    this.apple_music_url = apple_music_url;
    this.front_artwork_url = front_artwork_url;
    this.rear_artwork_url = rear_artwork_url;
    this.bandcamp_player = bandcamp_player_src;
  }
}

export { Artist, Album };
