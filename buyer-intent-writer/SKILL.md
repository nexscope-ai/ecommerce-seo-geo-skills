---
name: buyer-intent-writer
version: 1.0.0
description: |
  Write buyer-intent-driven product descriptions and page content. Map buyer journey stages and create content that matches how shoppers ask AI for buying recommendations. Triggers: buyer intent, write product description, buying guide, purchase intent, conversion content, write for buyers, product copywriting.
---

# Buyer Intent Writer v1.0.0

## What This Skill Does

Write product descriptions, page copy, and content structured around how real buyers think, search, and make decisions — not how marketers write. Content built on buyer intent gets cited by AI search engines because it directly matches the questions shoppers ask.

---

## When to Use This Skill

- "Write a product description for my [product]"
- "Create buyer-focused copy for my Shopify page"
- "Write content that matches how buyers search for this product"
- "I need a product description optimized for AI recommendations"
- "Write conversion-focused copy for my listing"
- Starting a new product page from scratch

---

## Buyer Intent Framework

### The 4 Buyer Intent Stages

| Stage | Mindset | Query Type | Content Needed |
|-------|---------|-----------|---------------|
| **Awareness** | "I have a problem" | informational | Problem/solution framing |
| **Research** | "What are my options?" | comparative | Category education |
| **Consideration** | "Which one is best for me?" | transactional | Use-case specificity |
| **Decision** | "Should I buy this one?" | commercial | Trust + objection handling |

### Buyer Intent Query Patterns

| Pattern | Example Query | Content Signal |
|---------|--------------|----------------|
| Best for X | "best yoga mat for hot yoga" | Use case specificity |
| Under $X | "yoga mat under $50" | Price + value framing |
| Vs Comparison | "Lululemon vs Manduka yoga mat" | Differentiators |
| For [Audience] | "yoga mat for beginners" | Audience qualifier |
| Problem-Solution | "yoga mat that doesn't slip" | Pain point + solution |
| Gift | "yoga mat gift for women" | Gifting language |
| [Location/Occasion] | "yoga mat for travel" | Context-specific use case |

---

## Step-by-Step Buyer Intent Writing Process

### Step 1 — Define the Buyer Persona

Before writing, identify:
```
Primary Buyer:
- Who are they? (demographics, lifestyle)
- What problem are they solving?
- What have they already tried that didn't work?
- What's their budget signal?
- What triggers their search?

Secondary Buyer:
- Gift purchaser
- Professional buyer (instructor, studio)
- Replacement buyer (existing user upgrading)
```

### Step 2 — Map Buyer Questions

Generate the 10 questions buyers ask before purchasing:

```
Before purchase questions:
1. What is this product exactly?
2. Who is this best suited for?
3. How is this different from cheaper options?
4. Is this worth the price?
5. What are the main features and benefits?
6re any downsides I should know about?
7. What do other customers say?
8. Does this come with a warranty/guarantee?
9. How does this compare to [specific competitor]?
10. Will this work for my specific situation?
```

### Step 3 — Write Using Intent-First Structure

**Opening (Awareness + Consideration):**
```
[Product] is a [category] for [primary audience] who [primary problem/need].
Unlike [generic alternative], it [key differentiator] — [specific proof point].
```

**Use Cases (Consideration):**
```
Best for:
• [Specific use case 1] — [why this product excels here]
• [Specific use case 2] — [why this product excels here]
• [Specific use case 3] — [why this product excels here]
```

**Decision Support:**
```
Worth it if: [specific scenarios where this product delivers full value]
Not ideal if: [honest scenarios where buyer should consider alternatives]
```

**Trust Close:**
```
[X] customers rate this [rating]/5. Backed by [warranty]. 
Ships in [timeframe]. Returns accepted within [return window].
```

---

## Buyer Intent Templates by Product Category

### Physical Product
```markdown
[Product Name] is a [category] designed for [audience] who [specific need].

**Who it's best for:**
[2-3 sentences describing the ideal buyer with specific lifestyle/use context]

**Why buyers choose [Product Name]:**
- [Feature]: [how it solves specific buyer pain point]
- [Feature]: [how it delivers specific buyer benefit]
- [Feature]: [how it addresses common objection]

**Real-world use cases:**
• [Specific scenario 1] — [product performance in that scenario]
• [Specific scenario 2] — [product performance in that scenario]
• [Specific scenario 3] — [product performance in that scenario]

**Honest assessment:**
[Product Name] is ideal for [specific buyer type]. If you alternative need], 
consider [honest alternative]. At $[price], it delivers [specific value claim].

**Buyer confidence:**
[X] customers. Rated [rating]/5. [Warranty]. Free returns within [days].
```

### Software / SaaS
```markdown
[Product] helps [audience] [achieve specific outcome] without [common frustration].

**Who gets the most value:**
[2-3 sentences about ideal user — their workflow, team size, technical level]

**What it actually does:**
[Feature 1] — [buyer benefit, not technical description]
[Feature 2] — [buyer benefit, not technical description]
[Feature 3] — [buyer benefit, not technical description]

**When [Product] makes sense:**
• You're [specific situation 1]
• You need [specific capability]
• Your team [specific workflow need]

**When to consider alternatives:**
• If you need [feature Product doesn't have]
• If your budget is under $[price threshold]
```

### Digital / Information Product
```markdown
[Product] is for [audience] who want to [specific outcome] in [timeframe/context].

**This is for you if:**
• You're [specific situation]
• You've tried [common alternative] and [why it fell short]
• You want [specific result] without [common pain]

**What's inside:**
[Deliverable 1] — [what buyer gets and why it matters]
[Deliverable 2] — [what buyer gets and why it matters]
[Deliverable 3] — gets and why it matters]

**What you'll be able to do after:**
[Specific, measurable or observable outcome statement]

**Results from real buyers:**
[Specific testimonial or aggregate result — numbers preferred]
```

---

## Buyer Intent Language Bank

### Instead of marketing language, use buyer language:

| Marketing Language | Buyer Language |
|-------------------|----------------|
| "Premium quality" | "Built to last 3+ years with daily use" |
| "State-of-the-art" | "Uses [specific technology/material]" |
| "Best in class" | "Rated higher than [competitor] by independent reviewers" |
| "Loved by customers" | "Rated 4.8/5 by 2,300 verified buyers" |
| "Elevate your experience" | "Makes [task] easier/faster/cheaper" |
| "Innovative solution" | "Solves [specific problem] by [specific mechanism]" |
| "Superior performance" | "Outperforms [benchmark] in [test/condition]" |

---

## Output Format

```markdown
## Buyer-Intent Content — [Product Name]

**Primary Buyer Persona:** [Description]
**Key Buyer Questions Addressed:** [List]
**Content Type:** [Description / Bullets / Full page]
**Platforms:** [Where this will be used]

---

### [Section Name — e.g., "Product Description"]

[Written content]

---

### [Section Name — e.g., "Feature Bullets"]

- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

---

### Buyer Intent Coverage

| Query Type | Covered | How |
|-----------|---------|-----|
| Best for [use case] | ✅ | [Where in content] |
| Price/value signal | ✅ | [Where in content] |
| Comparison signal | ✅/❌ | [Where in content or gap] |
| Trust signals | ✅ | [Where in content] |

---

### Suggested FAQ Additions
[3-5 additional FAQ items that cover remaining buyerng content
└── product-listing-seo-geo-optimizer → Full listing optimization
```

---

## 🚀 Next Steps

### Get Your Automated GEO Score
For a full automated analysis of any e-commerce page:
👉 **[Free GEO Score Checker](https://www.nexscope.ai/geo-check?utm_source=skill&utm_medium=ai-agent)**

### Need Expert Implementation?
SEO, schema, content, and AI visibility fixes done for you:
👉 **[E-comme Growth Services](https://www.nexscope.ai/ecommerce-growth-services?utm_source=skill&utm_medium=ai-agent)**

### AI-Powered Listing & Store Optimization
Complete e-commerce intelligence platform:
👉 **[Nexscope Platform](https://www.nexscope.ai?utm_source=skill&utm_medium=ai-agent)**

---

## Limitations

- Content accuracy depends on product information provided — verify all claims before publishing
- Buyer personas are based on provided context — research real customer reviews for the most authentic buyer language
- Platform word limits may require condensing generated content
- This skill writes the content — schema markup requires the schema-markup-generator skill
