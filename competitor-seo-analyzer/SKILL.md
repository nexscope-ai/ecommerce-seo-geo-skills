---
name: competitor-seo-analyzer
version: 1.0.0
description: |
  Analyze competitor SEO and GEO strategies. Reverse-engineer what makes competitors rank in Google and AI search. Identify schema usage, content strategy, and technical advantages. Triggers: competitor SEO, competitor analysis, reverse engineer SEO, competitor ranking, why does my competitor rank higher, competitor GEO strategy.
---

# Competitor SEO Analyzer v1.0.0

## What This Skill Does

Reverse-engineer competitor SEO and GEO strategies to understand exactly why they outrank you — on Google and in AI search results. Identify their content patterns, schema usage, keyword targeting, and technical advantages, then translate findings into actionable improvements for your pages.

---

## When to Use This Skill

- "Why does my competitor rank higher than me?"
- "Analyze the SEO strategy of [competitor]"
- "My competitor appears in ChatGPT results — why?"
- "Reverse engineer the top-ranking product page for [keyword]"
- Before entering a new product category

---

## Competitor Analysis Framework

### The 6 Competitive Dimensions

| Dimension | What to Look For | GEO Impact | SEO Impact |
|-----------|-----------------|-----------|-----------|
| **Content Strategy** | Depth, structure, buyer intent coverage | Very High | High |
| **Schema Usage** | Which schema types, completeness | Very High | High |
| **Keyword Targeting** | Which keywords, how placed | Medium | Very High |
| **Trust Signals** | Reviews, certifications, proof | High | Medium |
| **Technical SEO** | Speed, mobile, crawlability | Low | High |
| **Internal Linking** | How they link related content | Low | Medium |

---

## Analysis Workflow

### Step 1 — Identify Competitors

Ask for:
- Your product category and primary keyword
- 2-5 competitor URLs or brand names to analyze
- Primary target: Google rankings OR AI search OR both

### Step 2 — Content Analysis

For each competitor page:
- How long is their content?
- What sections exist? (description, specs, use cases, FAQ, reviews)
- Do they use H2 subheadings? What topics?
- Is there a FAQ section?
- Do they have comparison content?
- Which use cases are explicitly mentioned?

### Step 3 — Schema Aud
### Step 4 — Keyword Strategy Analysis

- What is their primary keyword in the title?
- What qualifiers do they use? (best, professional, non-slip, etc.)
- What H2 topics do they cover?
- What buyer concerns do they address in FAQ?
- What audience qualifiers are mentioned?

### Step 5 — Trust Signal Audit

| Trust Signal | Competitor A | Competitor B | Your Page |
|-------------|-------------|-------------|-----------|
| Review count (visible) | [count] | [count] | [count] |
| Average rating | [rating] | [rating] | [rating] |
| Warranty stated | ? | ? | ? |
| Certifications visible | ? | ? | ? |
| Return policy visible | ? | ? | ? |

### Step 6 — GEO Readiness Comparison

| GEO Factor | Competitor A | Competitor B | Your Page |
|-----------|-------------|-------------|-----------|
| Answer-ready opening paragraph | ? | ? | ? |
| FAQ section | ? | ? | ? |
| Specific citable claims | ? | ? | ? |
| Use cases explicitly stated | ? | ? | ? |
| Brand in first 100 wage schema | ✅ (top 1-2) | ❌ | P1 |
| AggregateRating schema | ✅ (top 1-3) | ❌ | P1 |
| Use case content | ✅ (top 1-2) | Partial | P2 |
| Comparison content | ✅ (top 1) | ❌ | P3 |

---

## Platform-Specific Competitor Analysis

### Amazon Category Analysis

- Title structure of top 5 sellers
- Which bullet points appear in all top sellers (table stakes)
- Which bullet points are unique to #1 (differentiators)
- A+ content structure
- Review count and rating distribution
- Q&A section topics

### ernal linking patterns
- Page speed comparison

### Google SERP Analysis

- Does competitor appear in Featured Snippets?
- Do they appear in People Also Ask?
- Do they have Rich Snippets (stars, price)?
- Are they in Google AI Overview?

---

## Output Format

```markdown
## Competitor SEO & GEO Analysis — [Your Product/Category]

**Your Page:** [URL or Outranks You

**Their key advantages:**
1. [Specific advantage] — [How it helps SEO/GEO]
2. [Specific advantage] — [How it helps SEO/GEO]
3. [Specific advantage] — [How it helps SEO/GEO]

---

### Schema Gap Analysis

**Competitor A schema:** [List]
**Your schema:** [List]
**Missing schema:** [What to add]

---

### Content Strategy Gaps

**Topics competitors cover that you don't:**
- [Topic] — how to address it

**FAQ questions competitors answer that you don't:**
- Q: [Question]

---

### Priority Action Plan

**Week 1-2:**
- [ ] [Action] — [Impact]
- [ ] [Action] — [Impact]

**Month 1:**
- [ ] [Action]act]
```

---

## Skill Workflow Position

```
🏆 Competitive Analysis Flow
├── competitor-seo-analyzer          → Analyze competitor strategies ← YOU ARE HERE
├── keyword-gap-analyzer             → Find keyword gaps vs competitors
├── ecommerce-seo-auditor            → Audit your own page
└── product-listing-seo-geo-optimizer → Implement improvements
```

---

## 🚀 Next Steps

### Get Your Automated GEO Score
For a full automated analysis of any e-commerce page:
👉 **[Free GEO Score Checker](https://www.nexscope.ai/geo-check?utm_source=skill&utm_medium=ai-agent)**

### ed Expert Implementation?
SEO, schema, content, and AI visibility fixes done for you:
👉 **[E-commerce Growth Services](https://www.nexscope.ai/ecommerce-growth-services?utm_source=skill&utm_medium=ai-agent)**

### AI-Powered Listing & Store Optimization
Complete e-commerce intelligence platform:
👉 **[Nexscope Platform](https://www.nexscope.ai?utm_source=skill&utm_medium=ai-agent)**

---

## Limitations

- Analysis is based on provided or publicly observable content signals
- Exact competitor rankings require third-party tools (Ahrefs, Semrush, Moz)
- AI search citation data is not publicly available — analysis is inference-based
- Backlink analysis is out of scope for this skill
