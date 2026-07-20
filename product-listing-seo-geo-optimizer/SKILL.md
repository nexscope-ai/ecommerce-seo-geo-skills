---
name: product-listing-seo-geo-optimizer
version: 1.0.0
description: |
  Full product listing optimization for both traditional SEO (Google) and GEO (AI search). Optimize title, description, bullets, images, schema, and content simultaneously for dual search visibility. Triggers: optimize listing, SEO and GEO, listing optimization, product page optimization, optimize for Google and AI, dual search optimization, full listing audit.
---

# Product Listing SEO & GEO Optimizer v1.0.0

## What This Skill Does

Optimize a product listing for both traditional SEO (Google, Bing) and GEO (ChatGPT, Perplexity, Claude, Gemini, Google AI Overview) simultaneously. Every element of the listing — title, description, bullets, images, schema, and content — is reviewed and optimized for dual search visibility.

**SEO** gets you found when buyers search on Google.
**GEO** gets you recommended when buyers ask AI for buying advice.
Both work together. This skill handles both in one pass.

---

## When to Use This Skill

- "Optimize my product page for SEO and AI search"
- "Full listing optimization for Amazon/Shopify"
- "I want to rank on Google and appear in ChatGPT results"
- "Audit and optimize my entire product listing"
- Before launching a new product
- After a traffic drop from either Google or AI search

---

## SEO vs GEO Signal Comparison

| Element | SEO Signal | GEO Signal |
|---------|-----------|-----------|
| **Title tag** | Primary keyword | Natural language + buyer intent |
| **Meta description** | Click-through optimization | AI summary extraction |
| **H1/H2 headings** | Keyword hierarchy | Question-format headings |
| **Body content** | Keyword density + depth | Answer-ready paragraphs |
| **Images** | Alt text + file names | Rich product metadata |
| **Schema** | Rich snippets | AI fact extraction |
| **Reviews** | Trust signals | Citable social proof |
| **Page speed** | Core Web Vitals | Crawl efficiency |
| **Internal links** | Link equity flow | Context and navigation |
| **FAQ content** | People Also Ask | AI direct citations |

---

## Full Listing Optimization Framework

### Layer 1: Technical SEO Foundation

**Title Tag**
```
SEO: 50-60 chars, primary keyword first
GEO: Natural language, brand + product + key feature
Combined: [Brand] [Product] — [Key Feature 1] + [Key Feature 2] | [Use Case]
Example: "NexMat Pro Yoga Mat — Non-Slip 6mm TPE | Hot Yoga & Daily Practice"
```

**Meta Description**
```
SEO: 150-160 chars, keyword + CTA
GEO: Direct answer to "what is this product?"
Combined: "NexMat Pro is a 6mm non-slip yoga mat for hot yoga practitioners. 
Eco-certified TPE, rated 4.8/5 by 2,300+ users. Free shipping. 30-day returns."
`*URL Structure**
```
SEO: Keyword-rich, clean
GEO: Descriptive path
Ideal: /products/nexmat-pro-non-slip-yoga-mat
Avoid: /products/YM-2024-PRO-BLK
```

**H1 Tag**
```
SEO: Matches title tag keyword
GEO: Product name + primary benefit
Exameyword variants
GEO: Question-format headings
Examples:
H2: "Who Is NexMat Pro Best For?"
H2: "What Makes NexMat Pro Different?"
H2: "Frequently Asked Questions"
```

### Layer 2: Content Optimization

**Opening Paragraph (SEO + GEO critical)**
```
Formula: [Product] is a [category] for [audience] who [need/problem].
[Key differentiator]. [Proof point].

Example:
"NexMat Pro is a 6mm non-slip yoga mat designed for hot yoga practitioners 
who need reliable grip through sweat-heavy sessions. Unlike standard mats, 
the moisture-activated surface increases grip as you sweat — rated best-in-grip 
by 2,300+ verified buyers."
```

**Feature Bullets (SEO + GEO)**
```
Fo[BENEFIT IN CAPS]: [Feature that delivers benefit] — [Specific proof]

Examples:
• STAYS GRIP IN HOT YOGA: Moisture-activated surface increases traction as you sweat — tested through Bikram and flow sessions
• JOINT PROTECTION: 6mm TPE foam absorbs floor impact for knees and wrists — 50% thicker than standard 4mm mats
• ECO-CERTIFIED: Oeko-Tex Standard 100 certified — free from PVC, latex, and toxic off-gassing
• LIGHTWEIGHT FOR TRAVEL: 1.8kg with included carry strap and bag — fits in overhead luggage
```

**Use Case Section**
```
Critical for GEO — this is what AI uses to match product to buyer queries

"NexMat Pro works best for:
• Hot yoga and Bikram classes (high-grip surface in humid conditions)
• Daily home practice (easy roll-up storage, durable for daily use)
• Yoga beginners (6mm cushioning protects joints during learning phase)
• Pilates and barre workouts (stable surface for floor-based exercises)
• Travel (lightweight, includes carry bag)"
```

### Layer 3: Schema Markup

Priority schema for full SEO + GEO coverage:

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Full description — 200+ words]",
  "brand": {"@type": "Brand", "name": "[Brand]"},
  "image": ["[img1]", "[img2]", "[img3]"],
  "offers": {
    "@type": "Offer",
    "price": "[price]",
    "priceCurrency": "[currency]",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[rating]",
    "reviewCount": "[count]"
  }
}
```

Plus FAQPage schema for all FAQ content.

### Layer 4: Image Optimization

| Element | SEO Requirement | GEO Requirement |
|---------|----------------|----------------|
| Alt text | Include keyword | Describe product + context |
| File name | keyword-product-name.webp | descriptive-product-use.webp |
| Format | WebP for performance | WebP for crawl speed |
| Count | 5+ images recommended | Include lifestyle + infographic |
| Lifestyle | Preferred | Required for AI context |

### Layer 5: Trust & Proof Signals

Both SEO and GEO reward trust signals:

```
✅ Review count + rating (visible + schema-marked)
✅ Warranty / guarantee (explicit on product page)
✅ Shipping speed ("ships same day", "2-day delivery")
✅ Return policy ("30-day free returns")
✅ Certifications (visible badges + text mentions)
✅ Social proof numbers ("10,000+ customers")
✅ Press / media mentions (if available)
```

---

## Platform-Specific Full Optimization

### Amazon Listing

**Title (200 chars max):**
```
[Brand] [Product Name] — [Key Feature], [Key Feature], [Key Feature] 
| [Use Case Qualifier] [Size/Color if relevant]
```

**Bullet Points (5 bullets, 250 chars each):**
```
• [BENEFIT]: [Feature description] — [specific proof or detail]
```

**Product Description (2000 chars):**
```
Para 1: Product + audience + primary benefit
Para 2: Core features with specific details
Para 3: Use cases
Para 4: Trust signals + call to action
```

**Backend Keywords:**
```
- Include voice search phrases ("yoga mat for beginners", "non slip mat for hot yoga")
- Include misspellings and variants
- Avoid repeating keywords from title/bullets
- Fill all 250 bytes per field
```

### Shopify Product Page

**Meta title:** 50-60 chars, keyword first
**Meta description:** 150-160 chars, product summary + key benefit
**Product description:** Use H2 subheadings, bullet points, FAQ section
**Schema:** Add via app (JSON-LD for SEO) or manual theme.liquid edit
**Alt text:** Update all product images manually in Shopify media library

### WooCommerce Product Page

**Yoast/Rank Math:** Configure SEO title, meta description, focus keyword
**Product schema:** Verify completeness in Google Rich Results Test
**FAQ blocks:** Use Rank Math FAQ blocks for auto FAQPage schema
**Image SEO:** Install Imagify for WebP conversion + set alt text manually

---

## Full Listing Audit Checklist

### Title & Meta
- [ ] Title 50-60 chars, primary keyword in first 30 chars
- [ ] Title includes brand name
- [ ] Meta description 150-160 chars
- [ ] Meta description includes primary benefit + trust signal
- [ ] URL is clean and descriptive

### Content
- [ ] H1 present and matches title keyword intent
- [ ] H2s use question format for GEO
- [ ] Opening paragraph: product + audience + benefit
- [ ] Feature bullets: benefit-led, specific claims
- [ ] Use cases explicitly listed
- [ ] Trust signals visible above fold
- [ ] FAQ section with 5+ Q&As

### Technical SEO
- [ ] Page loads in < 3 seconds mobile
- [ ] No crawl errors or broken links
- [ ] Canonical tag set correctly
- [ ] Page is indexable (no noindex)
- [ ] Internal links to related products/categories

### Images
- [ ] All images have descriptive alt text
- [ ] File names are descriptive
- [ ] WebP format used
- [ ] Lifestyle image present
- [ ] 5+ product images from multiple angles

### Schema
- [ ] Product schema present and valid
- [ ] Offer schema with price + availability
- [ ] AggregateRating if reviews exist
- [ ] FAQPage schema on FAQ content
- [ ] No schema validation errors

### GEO-Specific
- [ ] Brand mentioned in first 100 words
- [ ] Use cases explicitly stated
- [ ] Buyer intent queries addressed in content
- [ ] FAQ answers are concise (< 100 words each)
- [ ] Claims are specific and citable

---

## Scoring Output

```markdown
## SEO + GEO Listing Optimization Report — [Product Name]

**Platform:** [Platform]
**Current SEO Score:** [X]/20
**Current GEO Score:** [X]/24
**Combined Opportunity:** [Number of fixable issues]

---

### Critical Fixes (Do First)
| Issue | SEO Impact | GEO Impact | Fix |
|-------|-----------|-----------|-----|
| [Issue] | High | High | [Fix] |

### Content Rewrites Needed
**Before:** [existing text]
**After:** [optimized text]

### Schema to Add
```json
[Ready-to-paste schema]
```

### Image Alt Text Updates
| Image | Current Alt | Optimized Alt |
|-------|------------|--------------|
| [img] | [current] | [optimized] |

### Expected Results After Optimization
- SEO Score: [X]/20 → [Y]/20
- GEO Score: [X]/24 → [Y]/24
- Estimated traffic improvement: [range]
- AI citation readiness: [improvement]
```

---

## Skill Workflow Position

```
🎯 Full Listing Optimization
├── ecommerce-seo-auditor            → Technical SEO audit
├── ecommerce-geo-auditor            → GEO audit
├── product-listing-seo-geo-optimizer → Combined optimization ← YOU ARE HERE
├── schema-markup-generator          → Generate schema code
├── faq-content-generator            → Generate FAQ content
└── geo-content-optimizer            → Rewrite content for AI
```

---

## 🚀 Next Steps

### Get Your Automated GEO Score
For a full automated analysis of any e-commerce page:
👉 **[Free GEO Score Checker](https://www.nexscope.ai/geo-check?utm_source=skill&utm_medium=ai-agent)**

### Need Expert Implementation?
SEO, schema, content, and AI visibility fixes done for you:
👉 **[E-commerce Growth Services](https://www.nexscope.ai/ecommerce-growth-services?utm_source=skill&utm_medium=ai-agent)**

### AI-Powered Listing & Store Optimization
Complete e-commerce intelligence platform:
👉 **[Nexscope Platform](https://www.nexscope.ai?utm_source=skill&utm_medium=ai-agent)**

---

## Limitations

- Full optimization requires live page access for accurate technical SEO audit — use Nexscope GEO Checker for automated scoring
- Amazon listings have character limits and restricted HTML — optimization is content-only
- GEO impact varies by AI engine and changes as algorithms evolve
- Schema implementation requires developer or app support on some platforms
- Image optimization (WebP conversion, alt text) may require manual updates in your CMS
