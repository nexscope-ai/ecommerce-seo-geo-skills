---
name: structured-data-advisor
version: 1.0.0
description: |
  Advise which schema types to implement based on page type and platform. Prioritize schema implementation roadmap for maximum SEO and GEO impact. Triggers: which schema, schema roadmap, structured data strategy, what schema do I need, schema types, schema advice, schema priority.
---

# Structured Data Advisor v1.0.0

## What This Skill Does

Analyze your e-commerce setup and recommend exactly which schema types to implement, in what order, and why — based on your page type, platform, and current gaps.

---

## When to Use This Skill

- "What schema should I add to my product page?"
- "Where do I start with structured data?"
- "Which schemas matter most for AI search visibility?"
- "I have a Shopify store — what schema do I need?"
- "Create a schema implementation roadmap for my site"
- "Does my category page need schema?"

---

## Schema Priority Matrix by Page Type

### Product Detail Page

| Priority | Schema Type | GEO Impact | SEO Impact |
|----------|------------|-----------|-----------|
| 🔴 P1 | Product + Offer + AggregateRating | Critical | Rich snippets |
| 🟠 P2 | FAQPage | Very High | Featured snippets |
| 🟠 P2 | BreadcrumbList | High | Breadcrumb display |
| 🟡 P3 | Organization / Brand | High | Brand recognition |
| 🟢 P4 | Review (individual) | Medium | Review snippets |
| 🟢 P4 | VideoObject | Medium | Video carousels |

### Category / Collection Page

| Priority | Schema Type | GEO Impact | SEO Impact |
|----------|------------|-----------|-----------|
| 🔴 P1 | BreadcrumbList | High | Navigation display |
| 🟠 P2 | ItemList | High | List-style results |
| 🟠 P2 | FAQPage (if FAQ present) | Very High | Featured snippets |
| 🟡 P3 | Organization | Medium | Brand context |

### Homepage / Store

| Priority | Schema Type | GEO Impact | SEO Impact |
|----------|------------|-----------|-----------|
| 🔴 P1 | Organization | High | Brand identity |
| 🔴 P1 | WebSite (with SearchAction) | High | Sitelinks search |
| 🟠 P2 | FAQPage (if FAQ present) | Very High | Featured snippets |
| 🟡 P3 | LocalBusiness (if physical) | Medium | Local pack |

### Blog / Content Page

| Priority | Schema Type | GEO Impact | SEO Impact |
|----------|------------|-----------|-----------|
| 🔴 P1 | Article / BlogPosting | High | Article display |
| 🔴 P1 | FAQPage (if FAQ present) | Very High | Featured snippets |
| 🟠 P2 | BreadcrumbList | Medium | Navigation display |
| 🟡 P3 | HowTo (if tutorial) | High | How-to rich results |

---

## Platform-Specific Recommendations

### Shopify

**Already handled by platform (verify completeness):**
- Basic Product schema (may be incomplete — check for missing AggregateRating)
- Basic Offer schema

**You must add manually:**
- FAQPage schema (Shopify does not generate this)
- Complete AggregateRating with review count
- Organization schema on homepage
- VideoObject if using product videos

**Recommended approach:**
1. Install JSON-LD for SEO app — handles Product/Offer/Rating automatically
2. Add FAQPage schema manually in theme code for product pages with FAQ sections
3. Add Organization schema once in theme.liquid

### WooCommerce

**Handled by Yoast SEO / Rank Math:**
- Product schema (basic)
- Organization schema
- BreadcrumbList

**You must add or enhance:**
- FAQPage schema on product pages (use FAQ block with Rank Math)
- Complete AggregateRating (verify review count is populated)
- VideoObject for product videos

**Recommended approach:**
1. Use Rank Math Pro — most comprehensive WooCommerce schema support
2. Enable FAQ schema blocks in Gutenberg
3. Verify Product schema completeness in Search Console

### Amazon Listings

**Cannot add custom schema** — focus on content signals instead:
- Complete product title with key attributes
- Bullet points covering all buyer questions
- A+ Content with FAQ modules
- Backend keywords including voice search phrases
- Brand Registry for enhanced content

**GEO signals for Amazon come from content, not technical schema.**

### Etsy / eBay / Marketplace

**Limited schema control** — platform generates basic markup
- Focus on title optimization with buyer-intent language
- Complete all available product attribute fields
- Use full description length allowance
- Include all variant and specification details

### Custom / DTC Sites

**Full control** — implement the complete stack:
1. Product + Offer + AggregateRating (every product page)
2. FAQPage (every product page with FAQ)
3. Organization (once, in site header)
4. BreadcrumbList (all pages except homepage)
5. WebSite with SearchAction (homepage only)
6. VideoObject (product pages with videos)
7. Article / BlogPosting (all blog content)

---

## Implementation Roadmap Template

### Phase 1 — Foundation (Week 1)
```
✅ Product schema on all product pages
✅ Offer schema (price, availability, currency)
✅ AggregateRating schema (if you have reviews)
✅ Organization schema on homepage

Expected impact: Enables rich snippets, AI can extract product facts
```

### Phase 2 — GEO Boost (Week 2-3)
```
✅ FAQPage schema on top 10 product pages
✅ BreadcrumbList on all pages
✅ FAQPage schema on homepage/about page

Expected impact: AI direct answer citations, featured snippets
```

### Phase 3 — Advanced (Month 2)
```
✅ VideoObject for product video content
✅ Review schema for individual reviews
✅ ItemList for category pages
✅ HowTo for tutorial/guide content
✅ WebSite with SearchAction on homepage

Expected impact: Video carousels, how-to rich results, sitelinks search
```

---

## Schema Decision Tree

```
What type of page is this?

├── Product Page
│   ├── Has reviews? → Add AggregateRating
│   ├── Has FAQ section? → Add FAQPage
│   ├── Has video? → Add VideoObject
│   └── Always add: Product + Offer + BreadcrumbList
│
├── Category Page
│   ├── Has FAQ section? → Add FAQPage
│   └── Always add: BreadcrumbList + ItemList
│
├── Homepage
│   ├── Has FAQ section? → Add FAQPage
│   ├── Has physical location? → Add LocalBusiness
│   └── Always add: Organization + WebSite
│
└── Blog / Article
    ├── Has FAQ section? → Add FAQPage
    ├── Is a tutorial/guide? → Add HowTo
    └── Always add: Article + BreadcrumbList
```

---

## Output Format

```markdown
## Schema Implementation Roadmap — [Store/Site Name]

**Platform:** [Platform]
**Current Schema Status:** [None / Partial / Complete]
**Pages Analyzed:** [List]

---

### Your Schema Priority List

**🔴 Implement First (Critical)**
| Schema | Page(s) | Why It Matters |
|--------|---------|---------------|
| [Schema] | [Pages] | [GEO/SEO reason] |

**🟠 Implement Next (High Impact)**
| Schema | Page(s) | Why It Matters |
|--------|---------|---------------|

**🟡 Implement Later (Enhancement)**
| Schema | Page(s) | Why It Matters |
|--------|---------|---------------|

---

### 4-Week Implementation Plan

**Week 1:** [Actions]
**Week 2:** [Actions]
**Week 3-4:** [Actions]

---

### Platform-Specific Notes
[Specific guidance for their platform]

---

### Tools Needed
[Recommended plugins, apps, or code approach]
```

---

## Skill Workflow Position

```
📐 Schema & Structured Data Flow
├── structured-data-advisor   → Decide which schemas to add ← YOU ARE HERE
├── schema-markup-generator   → Generate the schema code
├── schema-validator          → Check for errors
└── ecommerce-geo-auditor     → Full GEO audit including schema review
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

- Recommendations are based on provided page type and platform information
- Final schema validation requires Google Rich Results Test
- Marketplace platforms (Amazon, eBay, Etsy) have limited schema support
- Schema alone doesn't guarantee rich results — content quality and page authority also matter
