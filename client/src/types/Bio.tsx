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

class Bio {
  name: string;
  bio: string;
  social_urls: SocialUrl[];

  constructor(name: string, bio: string, social_urls: SocialUrl[]) {
    this.name = name;
    this.bio = bio;
    this.social_urls = social_urls;
  }
}

export { Bio, SocialUrl };
