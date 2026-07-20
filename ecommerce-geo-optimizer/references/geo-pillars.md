# GEO Pillars — Detailed Definitions & Scoring Criteria

## Overview

Each pillar is scored 1-3 points. Maximum total score: 24/24.

---

## Pillar 1: Crawl & SEO Readiness (Foundation)

**Why it matters for GEO:**
AI engines rely on crawlers to access and index your content. If a page can't be crawled or indexed, it can't be cited — regardless of how good the content is.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Page is fully indexable, title and meta are optimized, H1 present, canonical correct, sitemap included, loads in <3s |
| 2 — Partial | Page is indexable but has 1-2 gaps (weak title, missing meta, slow load) |
| 1 — Weak | Indexing issues, missing fundamentals, or page blocked from crawlers |

### Key Checks
- `robots.txt` not blocking page
- No `noindex` tag
- Title tag: 50-60 chars, includes primary keyword + brand
- Meta description: 120-155 chars, answers "what is this product?"
- H1 present and matches title intent
- Canonical tag: self-referencing or correct redirect
- XML sitemap includes this URL
- Page speed: <3s on mobile (Core Web Vitals)
- HTTPS enabled

---

## Pillar 2: Image SEO & Product Understanding

**Why it matters for GEO:**
AI systems analyze product images both for visual signals and text metadata. Rich image metadata helps AI understand what the product looks like, how it's used, and who it's for.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | All images have descriptive alt text, filenames are meaningful, WebP/AVIF format, multiple product angles, lifestyle imagery present |
| 2 — Partial | Most images optimized but gaps remain (some missingMissing alt text on most images, generic filenames, no lifestyle imagery, heavy file sizes |

### Key Checks
- Alt text: describes product, use case, and brand ("Nexscope stainless steel water bottle 32oz blue")
- Filename: descriptive ("nexscope-32oz-water-bottle-blue.webp" not "IMG_001.jpg")
- Format: WebP or AVIF for performance
- Multiple angles: front, back, side, detail shots
- Lifestyle images: product in real use context
- Size reference image: product next to common object for scale
- Infographic image: key specs or features callout

---

## Pillar 3: Structured Data & Rich Signals

**Why it matters for GEO:**
Schema markup is the most direct signal AI systems use to extract product facts. Without it, AI must guess product details from unstructured text — with high error rates.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Complete Product + Offer + AggregateRating + Organization schema, FAQPage if FAQ present, no validation errors |
| 2 — Partial | Basic Product schema present but missing Offer, ratings, or has validation warnings |
| 1 — Weak | No schema or schema has critical errors |

### Required Schema Types

**Product Schema (essential)**
```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Product Name",
  "description": "Product description",
  "brand": {"@type": "Brand", "name": "Brand Name"},
  "sku": "SKU123",
  "image": ["url1", "url2"]
}
```

**Offer Schema (essential)**
```json
{
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://yourpage.com/product"
  }
}
```

**AggregateRating Schema (high impact)**
```json
{
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "2340"
  }
}
```

---

## Pilters for GEO:**
When a shopper asks "what are the best X products?", AI engines build a mental map of brands in a category. If your brand signals are weak, you won't appear in that map.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Brand name prominent in first 100 words, product category stated, full specs listed, use cases explicit, offer context clear |
| 2 — Partial | Brand present but category or specs vague, use cases implicit rather than explicit |
| 1 — Weak | Brand buried, category unclear, specs in images only, use cases not stated |

### Key Checks
- Brand name in: H1, first paragraph, product title
- Product category stated explicitly ("This is a [category] for [audience]")
- Materials and specifications in text (not only images)
- Colors and variants listed in text
- Primary use case stated in first 200 words
- Secondary use cases listed in bullets or FAQ
- Price range signal ("premium", "budget-friendly", or explicit price context)

---

## Pillar 5: Buyer Intent Coverage

**Why it matters for GEO:**
AI search queries are intent-driven: "best wireless earbuds under $100 for running". Pages that explicitly address these intent signals get cited more.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Content covers multiple use cases, comparison signals, budget fit, gifting scenarios, and directly answers buyer questions |
| 2 — Partial | Some intent coverage but missing key buyer questions or comparison content |
| 1 — Weak | Generic product description with no buyer intent signals |

### Buyer Intent Query Types to Cover

| Query Type | Example | Content Signal Needed |
|------------|---------|----------------------|
| Best for X | "best blender for smoothies" | Use case specificity |
| Budget/Value | "affordable yoga mat" | Price context and value signal |
| Comparison | "vs competitors" | Differentiators stated explicitly |
| Gift | "gift for coffee lovers" | Gifting language and scenarios |
| Problem/Solution | "back pain relief cushion" | Pain point + solution framing |
| Audience-specific | "for beginners / professionals" | Audience qualifier language |

---

## Pillar 6: Trust & Conversion Proof

**Why it matters for GEO:**
AI engines favor recommending products with strong trust signals. A product with verified reviews, clear policies, and certifications is safer for AI to cite than one without.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Review count + rating visible, warranty stated, shipping/returns clear, certifications present, social proof elements |
| 2 — Partial | Reviews present but warranty/policy info weak or buried |
| 1 — Weak | No visible reviews, policies unclear, no trust badges |

### Trust Signal Checklist
- ⭐ Review count and average rating (prominent, marked up with schema)
- 🛡️ Warranty or guarantee (explicit duration and coverage)
- 🚚 Shipping speed (same-day, 2-day, etc.)
- ↩️ Return policy (30-day, free returns, etc.)
- 🏅 Certifications (FDA, CE, BPA-free, organic, etc.)
- 👥 Social proof (X customers, Y units sold)
- 📰 Press mentions or expert endorsements
- 💬 User-generated content or Q&A section

---

## Pillar 7: AI Citation Readiness

**Why it matters for GEO:**
AI systems pull direct quotes and facts from pages to form answers. Pages structured with clear, citable claims in FAQ and summary formats get cited far more frequently.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | FAQ section with direct Q&A, concise answer paragraphs, specific citable claims, content summarizable without images |
| 2 — Partial | Some FAr direct answer content but claims are vague or content is image-dependent |
| 1 — Weak | No FAQ, vague claims, key information locked in images or videos |

### Citation-Ready Content Patterns

**FAQ Format (highest GEO impact)**
```
Q: Is this product safe for dishwashers?
A: Yes, the [Product Name] is fully dishwasher safe on the top rack.
```

**Concise Answer Paragraphs**
```
[Product Name] is a [category] designed for [audience]. 
It [key benefit] and [secondary benefit], making it ideal for [use case].
```

**Specific, Citable Claims**
- ✅ "Rated 4.8/5 by over 3,200 verified customers"
- ✅ "Keeps drinks cold for 24 hours and hot for 12 hours"
- ❌ "Great quality and very popular"
- ❌ "Customers love it"

---

## Pillar 8: Conversational Content

**Why it matters for GEO:**
Shoppers talk to AI in natural language. Pages written in conversational tone with natural language question phrases match AI query patterns more effectively.

### Scoring Criteria

| Score | Description |
|-------|-------------|
| 3 — Strong | Content uses natural language, directly addresses "who is this for?" and "why buy this?", long-tail question phrases in headings |
| 2 — Partial | Some conversational elements but product description remains primarily formal or keyword-focused |
| 1 — Weak | Purely formal/keyword-stuffed product description with no conversational elements |

### Conversational Content Examples

**Heading examples (conversational)**
- ✅ "Who Is This Product Best For?"
- ✅ "How Does It Compare to [Competitor]?"
- ✅ "What Do Customers Say After 6 Months of Use?"
- ❌ "Product Features"
- ❌ "Specifications"

**Opening paragraph (conversational)**
```
If you're looking for a [category] that [primary benefit], 
[Product Name] was built for exactly that. Whether you need 
[use case 1] or [use case 2], it delivers [key differentiator] 
without [common pain point].
```

---

## Score Interpretation

| Total Score | Rating | Recommended Action |
|-------------|--------|-------------------|
| 22-24 | 🟢 Excellent | Maintain and monitor AI citations monthly |
| 18-21 | 🟡 Good | Address weak pillars, especially schema and citation readiness |
| 13-17 | 🟠 Needs Work | Prioritize Pillars 3, 4, and 7 immediately |
| 8-12 | 🔴 Poor | Full GEO rewrite needed — start with schema and content |
| Below 8 | ⛔ Critical | Page is likely invisible to AI engines |
