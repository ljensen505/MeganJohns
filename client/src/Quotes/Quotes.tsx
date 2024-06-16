import { Quote } from "../types/Quote";
import QuoteElement from "./Quote";

interface QuotesProps {
  quotes: Quote[];
}

export default function Quotes(props: QuotesProps) {
  return (
    <section id="quotes" className="content-section">
      <h2>Quotes</h2>
      {props.quotes.map((quote) => (
        <QuoteElement
          key={quote.quotes_id}
          body={quote.body}
          author={quote.author}
          source_url={quote.source}
        />
      ))}
    </section>
  );
}
