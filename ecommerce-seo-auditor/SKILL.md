---
name: ecommerce-seo-auditor
version: 1.0.0
description: |
  Comprehensive technical and on-page SEO audit for e-commerce pages. Check title tags, meta descriptions, headers, keywords, internal linking, page speed, mobile optimization, and crawlability. Triggers: SEO audit, technical SEO, on-page SEO, site audit, SEO check, why am I not ranking, SEO diagnosis, SEO health check.
---

# E-commerce SEO Auditor v1.0.0

## What This Skill Does

Run a comprehensive SEO audit on e-commerce pages — covering technical SEO, on-page optimization, content quality, and crawlability. Identify exactly why pages aren't ranking and produce a prioritized fix list.

---

## When to Use This Skill

- "Audit my Shopify store SEO"
- "Why isn't my product page ranking on Google?"
- "Give me a full SEO health check"
- "Check my on-page SEO for this listing"
- "My organic traffic dropped — diagnose why"
- Before launching a new store or product page

---

## SEO Audit Framework — 6 Dimensions

### Dimension 1: Technical SEO

| Check | Good Signal | Bad Signal |
|-------|------------|-----------|
| Indexability | Page is indexable | noindex tag present |
| Robots.txt | Not blocking key pages | Critical pages blocked |
| Sitemap | All pages included | Missing or outdated |
| HTTPS | SSL active, no mixed content | HTTP or cert errors |
| Canonical | Self-referencing or correct | Missing or wrong target |
| Page Speed | < 3s on mobile | > 5s on mobile |
| Core Web Vitals | All pass | LCP/CLS/FID failing |
| Mobile Friendly | Passes Google mobile test | Layout issues on mobile |
| Structured Data | Valid schema present | Missing or has errors |
| Crawl Errors | No 4xx/5xx errors | Broken pages or redirects |

### Dimension 2: On-Page SEO

| Element | Best Practice | Common Mistake |
|---------|--------------|----------------|
| Title Tag | 50-60 chars, keyword first | Too long, keyword missing |
| Meta Description | 150-160 chars, compelling | Missing or duplicate |
| H1 | One H1, matches title intent | Multiple H1s or missing |
| H2-H6 | Hierarchical, keyword-rich | Random structure |
| URL | Short, descriptive, keyword | Parameter-heavy |
| Keyword Placement | In title, H1, first 100 words | Only in body |
| Content Length | 300+ words for product pages | Thin content under 150 |
| Duplicate Content | Unique per page | Copy-pasted descriptions |

### Dimension 3: Content Quality

| Factor | Check |
|--------|-------|
| Thin content | Under 300 words for product page |
| Duplicate content | Same as manufacturer or other pages |
| Keyword stuffing | Unnatural keyword density |
| Contentks | Links from category and related products |
| Category links | Linked from navigation and homepage |
| Orphan pages | Every page has at least one internal link |
| Anchor text | Descriptive anchors, not "click here" |

### Dimension 5: Image SEO

| Check | Requirement |
|-------|------------|
| Alt text | Descriptive, includes product name |
| File names | keyword-product.jpg not IMG001.jpg |
| File size | Under 200KB for web images |
| Format | WebP preferred |
| Lazy loading | Images below fold should lazy load |

### Dimension 6: E-commerce Specific

| Check | Requirement |
|-------|------------|
| Product schema | Product +AggregateRating |
| Reviews visible | With schema markup |
| Price in meta | Up-to-date |
| Stock
## Audit Workflow

### Step 1 — Gather Page Information

```
Required:
- URL or page content to audit
- Platform (Shopify, WooCommerce, Amazon, Custom)

Helpful:
- Current Google rankings (if known)
- Traffic trend (stable, dropping, never ranked)
- Competitors that outrank this page
- Any recent site changes
```

### Step 2 — Technical SEO Check

```
Is the page indexable? (no noindex, no robots block)
Is HTTPS active?
Is the canonical tag correct?
Is the page in the sitemap?
Does the URL follow best practices?
Are there obvious page speed issues?
Is the page mobile-friendly?
```

### Step 3 — On-Page SEO Check

```
Title tag: length, keyword placement, compelling?
Meta description: present, length, click-worthy?
H1: present, unique, matches intent?
H2s: question-format for GEO, keyword-rich for SEO?
Content length: 300+ words?
Keyword stuffing present?
Duplicate content from manufacturer?
```

### Step 4 — Content Quality Check

```
Does the page answer buyer questions?
Is content unique and original?
Is reading level appropriate?
Are there clear use cases and benefits?
Is there a FAQ section?
Are trust signals (reviews, warranty) present?
```

### Step 5 — Schema Check

```
Product schema present and valid?
Offer schema with price and availability?
AggregateRating if reviews exist?
FAQPage schema if FAQ present?
No validation errors?
```

### Step 6 — Score and Prioritize

Score each dimension 1-5:
- **5**: Fully optimized
- **4**: Minor gaps
- **3**: Needs improvement
- **2**: Significant issues
- **1**: Critical problems

**Total out of 30:**

| Score | Rating | Action |
|-------|--------|--------|
| 25-30 | Strong | Monitor and maintain |
| 20-24 | Good | Address weak areas |
| 14-19 | Needs Work | Prioritize top fixes |
| Below 14 | Poor | Full SEO overhaul needed |

---

## Common E-commerce SEO Issues

### Issue 1: Thin Product Descriptions
**Problem:** Under 300 words — not enough signal for Google to rank confidently
**Fix:** Expand with use cases, specifications, FAQ, and buyer intent content
**Impact:** High

### Issue 2: Duplicate Title Tags
**Problem:** Same or auto-generated titles across products
**Fix:** Unique title per page: `[Brand] [Product] — [Key Feature] | [Category]`
**Impact:** High

### Issue 3: Missing Schema
**Problem:** No structured data on product pages
**Fix:** Add Product + Offer + AggregateRating JSON-LD
**Impact:** Very High for both rich snippets and GEO

### Issue 4: Faceted Navigation Crawl Issues
**Problem:** Filter parameters creating duplicate URLs
**Fix:** Noindex filter pages or use canonical to main category
**Impact:** High — wastes crawl budget

### Issue 5: Orphaned New Products
**Problem:** New products have no internal links
**Fix:** Link from related products, categories, and blog
**Impact:** Medium

### Issue 6: Images Not Optimized
**Problem:** Large JPEG files, no alt text, generic filenames
**Fix:** Convert to WebP, write descriptive alt text
**Impact:** Medium

### Issue 7: Missing Meta Descriptions
**Problem:** Google auto-generates poorly
**Fix:** Write compelling 150-160 char meta descriptions
**Impact:** Medium — affects click-through rate

---

## Output Format

```markdown
## SEO Audit Report — [Page/Store Name]

**Platform:** [Platform]
**Audit Date:** [Date]

---

### Overall SEO Score: [X]/30 — [Rating]

| Dimension | Score | Status | Top Issue |
|-----------|-------|--------|-----------|
| Technical SEO | X/5 | ✅/⚠️/❌ | [Issue] |
| On-Page SEO | X/5 | ✅/⚠️/❌ | [Issue] |
| Content Quality | X/5 | ✅/⚠️/❌ | [Issue] |
| Internal Linking | X/5 | ✅/⚠️/❌ | [Issue] |
| Image SEO | X/5 | ✅/⚠️/❌ | [Issue] |
| E-commerce Specifics | X/5 | ✅/⚠️/❌ | [Issue] |

---

### Critical Issues (Fix First)

**Issue 1: [Issue Name]**
- Problem: [What's wrong]
- Fix: [Exact action]
- Impact: High/Medium/Low

---

### Prioritized Fix Roadmap

**This Week (Quick wins):**
- [ ] [Fix] — [Time] — [Impact]

**Next 2 Weeks:**
- [ ] [Fix] — [Time] — [Impact]

**This Month:**
- [ ] [Fix] — [Time] — [Impact]

---

### Projected SEO Score After Fixes: [X]/30
```

---

## Platform-Specific Notes

### Shopify
- Check: Is Online Store > Preferences title/description set?
- Check: Are collection page descriptions populated?
- Check: Is sitemap submitted to Google Search Console?
- Watch for: Duplicate content from /products/ and /collections/products/ URLs

### WooCommerce
- Check: Is Yoast/Rank Math configured with product schema?
- Check: Are product categories indexed?
- Watch for: Pagination issues on category pages
- Quick win: Enable Rank Math schema for all product types

### Amazon
- Limited technical SEO control — focus on content signals
- Check: Title within 200 characters?
- Check: All 5 bullet points used?
- Check: Backend keywords fully used?

---

## Skill Workflow Position

```
🔍 SEO Audit Flow
├── ecommerce-seo-auditor            → Technical + on-page SEO ← YOU ARE HERE
├── ecommerce-geo-auditor            → AI search visibility
├── product-listing-seo-geo-optimizer → Combined optimization
├── keyword-gap-analyzer             → Find keyword opportunities
└── competitor-seo-analyzer          → Benchmark vs competitors
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

- Full technical SEO audit requires live page crawl — this skill works from provided content
- Core Web Vitals require live testing (PageSpeed Insights, GTmetrix)
- Backlink analysis is outside scope — this focuses on on-page factors
- Rankings are affected by domain authority and backlinks beyond on-page SEO
