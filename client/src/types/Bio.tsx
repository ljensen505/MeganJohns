class SocialUrl {
  social_id: number;
  social_name: string;
  social_url: string;

  constructor(social_id: number, social_name: string, social_url: string) {
    this.social_id = social_id;
    this.social_name = social_name;
    this.social_url = social_url;
  }
}

class BioParagraph {
  bio_paragraph_id: number;
  bio_paragraph: string;

  constructor(bio_paragraph_id: number, bio_paragraph: string) {
    this.bio_paragraph_id = bio_paragraph_id;
    this.bio_paragraph = bio_paragraph;
  }
}

class Bio {
  name: string;
  bio: BioParagraph[];
  social_urls: SocialUrl[];

  constructor(name: string, bio: BioParagraph[], social_urls: SocialUrl[]) {
    this.name = name;
    this.bio = bio;
    this.social_urls = social_urls;
  }
}

export { Bio, BioParagraph, SocialUrl };
