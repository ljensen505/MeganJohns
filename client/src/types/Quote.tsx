class Quote {
  quotes_id: number;
  body: string;
  author: string;
  source?: string;

  constructor(
    quotes_id: number,
    body: string,
    author: string,
    source?: string
  ) {
    this.quotes_id = quotes_id;
    this.body = body;
    this.author = author;
    this.source = source;
  }
}

export { Quote };
