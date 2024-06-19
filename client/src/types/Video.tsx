class Video {
  id: number;
  type: string = "video";
  title: string;
  subtitle: string;
  description: string;
  youtube_player?: string;

  constructor(
    id: number,
    title: string,
    subtitle: string,
    description: string,
    youtube_player?: string
  ) {
    this.id = id;
    this.type = "video";
    this.title = title;
    this.subtitle = subtitle;
    this.description = description;
    this.youtube_player = youtube_player;
  }
}

export { Video };
