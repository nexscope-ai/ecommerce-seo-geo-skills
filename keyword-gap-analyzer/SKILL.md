---
name: keyword-gap-analyzer
version: 1.0.0
description: |
  Identify keywords competitors rank for that your pages miss. Find high-opportunity gaps for both traditional search and AI query patterns. Prioritize by traffic potential and buyer intent. Triggers: keyword gap, missing keywords, competitor keywords, keyword opportunity, keyword analysis, what keywords am I missing, keyword research.
---

# Keyword Gap Analyzer v1.0.0

## What This Skill Does

Identify keyword opportunities your e-commerce pages are missing — both traditional search keywords (Google) and AI query patterns (ChatGPT, Perplexity). Analyze competitor keyword strategies, find high-value gaps, and create a prioritized keyword roadmap.

---

## When to Use This Skill

- "What keywords am I missing on my product page?"
- "Find keyword gaps vs my competitors"
- "What should I rank for that I don't?"
- "Analyze competitor keyword strategy"
- "Build a keyword list for my product category"
- "Find AI query patterns my content doesn't cover"

---

## Keyword Gap Framework

### 3 Types of Keyword Gaps

**Gap Type 1: Missing Keywords**
Keywords competitors rank for, you don't target at all.
Action: Create or optimize content to target these.

**Gap Type 2: Underoptimized Keywords**
Keywords you rank for but not in the top 10.
Action: Improve on-page optimization for existing content.

**Gap Type 3: Missing AI Query Patterns**
Conversational queries AI gets asked that your content doesn't answer.
Action: Add FAQ content and use-case sections.

---

## Keyword Research Process

### Step 1 — Understand the Product & Category

Before analyzing gaps, identify:
```
- Primary product name and category
- Target marketplace (Amazon, Google, TikTok, etc.)
- Target audience (demographics, use cases)
- Price point (budget, mid-range, premium)
- Geographic focus (US, UK, EU, global)
- Top 3-5 competitor products or brands
```

### Step 2 — Seed Keyword Mapping

Generate seed keywords across intent types:

**Transactional (buyer ready to purchase):**
```
- [product] buy
- [product] best
- [product] [key feature]
- [product] for [use case]
- [product] under $[price]
```

**Comparative (buyer evaluating options):**
```
- best [product category]
- [product] vs [competitor]
- [product] review
- [product] pros and cons
- [product] alternatives
```

**Informational (buyer researching):**
```
- how to choose [product]
- what to look for in [product]
- [product] buying guide
- [use case] tips
- how does [product] work
```

**AI Search Patterns (conversational queries):**
```
- best [product] for [specific use case]
- [product] for [audience]
- what's the difference between [A] and [B]
- is [product] worth buying
- [problem] — what should I buy?
```

### Step 3 — Competitor Keyword Analysis

For each competitor, identify:

**Content signals they rank for:**
- Product title keywords
- Description keywords
- H2 heading topics
- FAQ content topics
- Blog content topics

**Schema signals they use:**
- Product categories and attributes
- FAQ question topics
- Review themes

**Estimate their keyword coverage:**

| Keyword Type | Competitor A | Competitor B | Your Page | Gap? |
|-------------|-------------|-------------|-----------|------|
| Primary product keyword | ✅ | ✅ | ✅ | No |
| Use case keyword | ✅ | ✅ | ❌ | Yes |
| Comparison keyword | ✅ | ❌ | ❌ | Yes |
| Buyer concern keyword | ✅ | ✅ | ❌ | Yes |
| AI query pattern | ✅ | ❌ | ❌ | Yes |

### Step 4 — Prioritize by Opportunity Score

Score each gap keyword:

| Factor | Weight | How to Score |
|--------|--------|-------------|
| Search intent match | 30% | Transactional > Comparative > Informational |
| Buyer stage match | 25% | Decision > Consideration > Awareness |
| Competitive difficulty | 25% | Low = easier to win |
| Traffic potential | 20% | Based on category search volume |

**Priority tiers:**
- 🔴 **P1 — High Priority**: Transactional, low competition, decision-stage
- 🟠 **P2 — Medium Priority**: Comparative or informational, medium competition
- 🟡 **P3 — Low Priority**: Informational, high competition

---

## Keyword Gap Categories for E-commerce

### Category 1: Use-Case Keywords
These are highest-impact for both SEO and GEO.

```
Pattern: "[product] for [specific use case]"

Examples:
- "yoga mat for hot yoga" (high commercial intent)
- "yoga mat for beginners" (specific audience)
- "yoga mat for travel" (specific context)
- "yoga mat for knee pain" (problem-solution)
- "yoga mat for tall people" (specific need)
```

**How to address:** Add use-case sections to product pages and FAQ content.

### Category 2: Comparison Keywords
Buyers in the consideration stage actively search these.

```
Pattern: "[product A] vs [product B]"
Pattern: "best [product] for [use case]"
Pattern: "[product] alternatives"

Examples:
- "Lululemon vs Manduka yoga mat"
- "best yoga mat for hot yoga 2024"
- "Gaiam alternatives"
```

**How to address:** Add comparison content to product descriptions or create dedicated comparison pages.

### Category 3: Problem-Solution Keywords
High buyer intent — buyer knows their problem, seeking solution.

```
Pattern: "[problem] solution"
Pattern: "[problem] what should I buy"
Pattern: "how to fix [problem]"

Examples:
- "yoga mat that doesn't slip on carpet"
- "yoga mat for sweaty hands"
- "non-toxic yoga mat"
```

**How to address:** Address problem explicitly in product description and FAQ.

### Category 4: Audience Qualifier Keywords
Specific audience segments searching with high intent.

```
Pattern: "[product] for [audience]"

Examples:
- "yoga mat for seniors"
- "yoga mat for plus size"
- "yoga mat for kids"
- "professional yoga mat"
```

**How to address:** Create audience-specific content sections or dedicated pages for large audiences.

### Category 5: AI Query Patterns
Conversational queries that AI engines receive.

```
Patterns:
- "What is the best yoga mat for someone who sweats a lot?"
- "I need a non-slip yoga mat under $50 — what do you recommend?"
- "Is a 4mm or 6mm yoga mat better for beginners?"
- "What yoga mat do professional instructors use?"
```

**How to address:** FAQ sections with direct Q&A format addressing these specific questions.

---

## Keyword Gap Output Format

```markdown
## Keyword Gap Analysis — [Product/Store Name]

**Category:** [Product category]
**Platform:** [Primary channel]
**Competitors Analyzed:** [List]

---

### Your Current Keyword Coverage

**Strong coverage (keep):**
- [Keyword]: [Where it appears]
- [Keyword]: [Where it appears]

**Partial coverage (improve):**
- [Keyword]: [Current ranking/mention] → [How to improve]

---

### Keyword Gaps Found

#### 🔴 High Priority Gaps

| Keyword | Intent | Difficulty | Where to Add |
|---------|--------|-----------|-------------|
| [keyword] | Transactional | Low | Product description |
| [keyword] | Comparative | Medium | FAQ section |

#### 🟠 Medium Priority Gaps

| Keyword | Intent | Difficulty | Where to Add |
|---------|--------|-----------|-------------|
| [keyword] | Informational | Medium | H2 heading + content |

#### 🟡 Low Priority / Content Opportunities

| Keyword | Intent | Difficulty | Content Needed |
|---------|--------|-----------|----------------|
| [keyword] | Informational | High | New blog post |

---

### AI Query Patterns to Address

| Query Pattern | How to Address |
|--------------|----------------|
| "[conversational query]" | Add FAQ: "Q: [query] A: [answer]" |
| "[conversational query]" | Add use-case section covering this |

---

### Implementation Plan

**Add to product page this week:**
- [ ] [Keyword] — add to [H2 / desc[Keyword] — add to [H2 / description / FAQ]

**Create new FAQ questions:**
- Q: [question covering AI query pattern]
- Q: [question covering comparison keyword]

**Consider new content:**
- [Keyword cluster] → Product comparison page
- [Keyword cluster] → Buying guide blog post

---

### Expected SEO + GEO Impact
Covering these gaps should improve:
- Traditional search rankings for [X] new keyword targets
- AI search citations for [X] query patterns
- Estimated traffic increase: [range based on category]
```

---

## Skill Workflow Position

```
🔍 Keyword Research Flow
├── keyword-gap-analyzer             → Find missing keywords ← YOU ARE HERE
├── competitor-seo-analyzer          → Analyze competitor strategy
├── product-listing-seo-geo-optimizer → Implement keywords in listing
├── geo-content-optimizer            → Rewrite content with new keywords
└── faq-content-generator            → Create FAQ for AI query patterns
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

## Limitaor exact search volumes, use Google Keyword Planner, Ahrefs, or Semrush
- AI query patterns are inferred from buyer behavior — actual AI search volumes are not publicly available
- Competitive difficulty estimates are qualitative without third-party SEO data
