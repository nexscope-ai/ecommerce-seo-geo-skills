# Safe ecommerce schema patterns

Use these as structural examples only. Replace example values with verified visible facts and inspect existing platform markup before adding code.

## Product with Offer

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

## BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Example Product"
    }
  ]
}
```

Validate current Google feature requirements separately. Valid schema does not guarantee a rich result or AI citation.
