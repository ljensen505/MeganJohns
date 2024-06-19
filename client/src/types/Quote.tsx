class Quote {
  id: number;
  body: string;
  author: string;
  source?: string;

  constructor(id: number, body: string, author: string, source?: string) {
    this.id = id;
    this.body = body;
    this.author = author;
    this.source = source;
  }
}

export { Quote };
