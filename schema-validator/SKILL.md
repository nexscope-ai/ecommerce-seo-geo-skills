---
name: schema-validator
version: 1.0.0
description: |
  Diagnose schema markup errors and completeness issues. Check for missing required fields, wrong data types, validation errors, and provide corrected schema code. Triggers: validate schema, schema errors, fix schema, schema validation, structured data errors, schema checker, check my schema.
---

# Schema Validator v1.0.0

## What This Skill Does

Diagnose and fix schema markup issues on e-commerce pages. Review existing JSON-LD schema for errors, missing required fields, incorrect values, and GEO impact gaps — then provide corrected, ready-to-paste code.

---

## When to Use This Skill

- "Check my schema for errors"
- "My schema isn't showing in Google Rich Results"
- "Validate this JSON-LD markup"
- "Why isn't my product schema working?"
- "Fix the errors in my structured data"
- After adding schema to a new page
- When Google Search Console reports schema warnings

---

## Validation Framework

### Required Fields by Schema Type

**Product Schema — Required Fields:**
```
✅ @context: "https://schema.org/"
✅ @type: "Product"
✅ name: (product name string)
✅ description: (min 50 characters)
✅ image: (URL or array of URLs)
✅ brand.@type: "Brand"
✅ brand.name: (brand name string)
```

**Offer Schema — Required Fields:**
```
✅ @type: "Offer"
✅ price: (numeric value, NOT a string with currency symbol)
✅ priceCurrency: (ISO 4217 code: USD, GBP, EUR, etc.)
✅ availability: (schema.org URL)
✅ url: (product page URL)
```

**AggregateRating Schema — Required Fields:**
```
✅ @type: "AggregateRating"
✅ ratingValue: (numeric, 0-5)
✅ reviewCount: (integer, min 1)
✅ bestRating: "5" (recommended)
✅ worstRating: "1" (recommended)
```

**FAQPage Schema — Required Fields:**
```
✅ @type: "FAQPage"
✅ mainEntity: (array of Question objects)
✅ mainEntity[].@type: "Question"
✅ mainEntity[].name: (question string)
✅ mainEntity[].acceptedAnswer.@type: "Answer"
✅ mainEntity[].acceptedAnswer.text: (answer string)
```

---

## Common Schema Errors

### Error 1: Price as String with Currency Symbol
```json
// ❌ Wrong
"price": "$29.99"

// ✅ Correct
"price": "29.99",
"priceCurrency": "USD"
```

### Error 2: Wrong Availability URL
```json
// ❌ Wrong
"availability": "InStock"
"availability": "in stock"

// ✅ Correct
"availability": "https://schema.org/InStock"
"availability": — no @context
{
  "@type": "Product",
  "name": "..."
}

// ✅ Correct
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "..."
}
```

### Error 4: Rating Value Out of Range
```json
// ❌ Wrong
"ratingValue": "4.8/5"
"ratingValue": 48

// ✅ Correct
"ratingValue": "4.8",
"bestRating": "5: "https://example.com/image1.jpg"

// ✅ Correct
"image": [
  "https://example.com/image1.jpg",
  "https://example.com/image2.jpg"
]
```

### Error 6: Duplicate Product Schema
```json
// ❌ Wrong — two Product schema blocks on same page
<script type="application/ld+json">{"@type": "Product", ...}</script>
<script type="application/ld+json">{"@type": "Product", ...}</script>

// ✅ Correct — one Product schema per page
<script type="application/ld+json">{"@type": "Product", ...}</script>
```

### Error 7: HTML Entities in Text
```json
// ❌ Wrong
"description": "Best &amp; most affordable product"

// ✅ Correct
"description": "Best and most affordable product"
```

### Error 8: Nested Schema Not Properly Structured
```json
// ❌ Wrong — Offer not nested inside Product
{
  "@type": "Product",
  "name": "...",
  "price": "29.99"
}

// ✅ Correct — Offer nested under offers property
{
  "@type": "Product",
  "name": "...",
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "USD"
  }
}
```

### Error 9: FAQ Answer Too Long
```json
// ⚠️ Warning — answers over 300 words may not be used by AI
"text": "[5 paragraph answer that goes on and on...]"

// ✅ Better — concise direct answer
"text": "Yes, this product is dishwasher safe on the top rack only. Hand washing is recommended for best results."
```

### Error 10: ReviewCount is Zero or Missing
```json
// ❌ Wrong
"reviewCount": "0"
"reviewCount": ""

// ✅ Correct — only add AggregateRating if you have actual reviews
// Remove AggregateRating entirely if no reviews exist
```

---

## Validation Checklist

Run through this checklist for any schema:

### Structural Checks
- [ ] Valid JSON (no syntax errors, missing commas, unclosed brackets)
- [ ] `@context` presed
- [ ] No duplicate schema types on same page

### Product Schema Checks
- [ ] `name` is product-specific, not store name
- [ ] `descrige.jpg)
- [ ] `sku` or `mpn` present if available
- [ ] No HTML tags or entities in text fields

### Offer Schema Checks
- [ ] `price` is numeric, no currency symbols
- [ ] `priceCurrency` is correct ISO code
- [ ] `availability` uses full schema.org URL
- [ ] `url` matches actual product page URL
- [ ] `priceValidUntil` is future date (if used)

### AggregateRating Checks
- [ ] `ratingValue` is decimal between 1-5
- [ ] `reviewCount` is integks
- [ ] `mainEntity` is an array
- [ ] Each item has `@type: "Question"`
- [ ] Each `acceptedAnswer` has `@type: "Answer"`
- [ ] Question text ends with `?`
- [ ] Answers are concise (under 300 words)
- [ ] FAQ content matches actual page content

---

## Validation Output Format

```markdown
## Schema Validation Report — [Page/Product Name]

**Schema Types Found:** [List]
**Validation Status:** ✅ Valid / ⚠️ Warnings / ❌ Errors Found

---

### Critical Errors (must fix)

**Error 1: [Error Name]**
- Location: [Schema type and field]
- Problem: [What is wrong]
- Fix:
```json
// Before
"field": "wrong_value"

// After
"field": "correct_value"
```

---

### Warnings (should fix)

**Warning 1: [Warning Name]**
- Location: [Schema type and field]
- Problem: [What could be improved]
- Recommendation: [Suggested fix]

---

### GEO Impact Assessment

| Schema Type | Status | GEO Impact |
|-------------|--------|------------|
| Product | ✅/⚠️/❌ | [impact if fixed] |
| Offer | ✅/⚠️/❌ | [impact if fixed] |
| AggregateRating | ✅/⚠️/❌ | [impact if fixed] |
| FAQPage | ✅/⚠️/❌ | [impact if fixed] |

---

### Corrected Complete Schema

```json
[Complete fixed schema ready to paste]
```

---

### Next Steps
1. Replace existing schema with corrected version above
2. Test at: https://search.google.com/test/rich-results
3. Check Google Search Console > Enhancements after 48-72 hours
```

---

## Validation Tools Reference

| Tool | URL | Best For |
|------|-----|---------|
| Google Rich Results Test | search.google.com/test/rich-results | Final validation before launch |
| Schema.org Validator | validator.schema.org | Comprehensive property check |
| Google Search Console | search.google.com/search-console | Monitor live schema health |
| JSON Formatter | jsonformatter.curiousconcept.com | Syntax checking |

---

## Skill Workflow Position

```
📐 Schema & Structured Data Flow
├── structured-data-advisor   → Decide which schemas to add
├── schema-markup-generator   → Generate the schema code
├── schema-validator          → Check for errors ← YOU ARE HERE
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

- Validation is based on provided schema code — cannot crawl live pages
- Some schema errors only appear in Google's live testing tool
- Schema validity does not guarantee rich results in search
- Marketplace pages (Amazon, eBay) cannot use custom schema
- Schema should be re-validated after any product detail changes
