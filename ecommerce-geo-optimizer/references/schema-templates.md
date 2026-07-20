# Safe ecommerce schema patterns

Use verified visible facts and inspect existing platform-generated markup before implementation.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Example Product",
  "image": ["https://example.com/product.webp"],
  "brand": {
    "@type": "Brand",
    "name": "Example Brand"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/example",
    "priceCurrency": "USD",
    "price": "29.99",
    "availability": "https://schema.org/InStock"
  }
}
```

Do not add ratings, reviews, identifiers, shipping, or return policies unless they are real, visible, and correctly modeled. Validate Google feature eligibility and general schema.org vocabulary separately.
