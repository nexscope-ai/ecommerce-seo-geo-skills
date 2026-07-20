---
name: schema-markup-generator
version: 1.0.0
description: |
  Generate complete, ready-to-paste JSON-LD schema markup for e-commerce pages. Covers Product, Offer, AggregateRating, FAQPage, BreadcrumbList, Organization schemas. Triggers: schema markup, JSON-LD, structured data, product schema, generate schema, add schema to my page.
---

# Schema Markup Generator v1.0.0

## What This Skill Does

Generate complete, validated, ready-to-paste JSON-LD schema markup for any e-commerce page. Schema markup is the single highest-impact GEO and SEO optimization you can make — it tells AI engines exactly what your product is, who sells it, what it costs, and why buyers trust it.

---

## When to Use This Skill

- "Generate Product schema for my Shopify page"
- "I need JSON-LD markup for my Amazon listing"
- "Add FAQ schema to my product page"
- "Create complete structured data for my e-commerce store"
- "My page has no schema — generate everything I need"
- Before launching any new product page or store

---

## Schema Types for E-commerce

### Priority 1 — Essential (implement first)

| Schema Type | Purpose | GEO Impact |
|-------------|---------|------------|
| **Product** | Identifies product name, brand, description, images | 🔴 Critical |
| **Offer** | Price, availability, seller info | 🔴 Critical |
| **AggregateRating** | Review count and average rating | 🔴 Critical |

### Priority 2 — High Impact

| Schema Type | Purpose | GEO Impact |
|-------------|---------|------------|
| **FAQPage** | Q&A content for AI direct answers | 🟠 Very High |
| **Organization / Brand** | Brand identity and authority | 🟠 Very High |
| **BreadcrumbList** | Navigation context and category path | 🟡 High |

### Priority 3 — Enhancement

| Schema Type | Purpose | GEO Impact |
|-------------|---------|------------|
| **Review** | Individual customer reviews | 🟡 Medium |
| **VideoObject** | Product video content | 🟡 Medium |
| **ItemList** | Category or collection pages | 🟢 Medium |

---

## Step-by-Step Schema Generation

### Step 1 — Gather Page Information

Ask the user for:
```
Required:
- Product name
- Brand name
- Product description (at least 50 words)
- Price and currency
- Availability (in stock / out of stock)
- Product URL
- Main product image URL

Helpful:
- Review count and average rating
- SKU / MPN / GTIN
- Product category
- Multiple image URLs
- FAQ content
```

### Step 2 — Generate Core Product Schema

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[150-300 word product description]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "sku": "[SKU or Model Number]",
  "mpn": "[Manufacturer Part Number if available]",
  "image": [
    "[main_image_url]",
    "[second_image_url]",
    "[lifestyle_image_url]"
  ],
  "url": "[product_page_url]",
  "offers": {
    "@type": "Offer",
    "price": "[29.99]",
    "priceCurrency": "[USD]",
    "availability": "https://schema.org/InStock",
    "url": "[product_page_url]",
    "seller": {
      "@type": "Organization",
      "name": "[Store Name]"
    },
    "priceValidUntil": "[2025-12-31]",
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
  eviewCount": "[1250]",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### Step 3 — Generate FAQ Schema

Use when the page has a FAQ section or Q&A content:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Concise, direct answer to Question 1]"
      }
    },
    {
      "@type": "Question",
      "name": "[Question 2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Concise, direct answer to Question 2]"
      }
    }
  ]
}
```

**FAQ content tips for maximum GEO impact:**
- Keep answers under 100 words for AI readability
- Use natural language in both questions andme": "[Brand/Store Name]",
  "url": "[store_url]",
  "logo": {
    "@type": "ImageObject",
    "url": "[logo_url]"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": ["English"]
  },
  "sameAs": [
    "[twitter_url]",
    "[instagram_url]",
    "[facebook_url]",
    "[linkedin_url]"
  ]
}
```

### Step 5 — Generate BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "[home_url]"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Category Name]",
      "item": "[category_url]"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Product Name]",
      "item": "[product_url]"
    }
  ]
}
```

---

## Platform-Specific Implementation

### Shopify
```html
<!-- Add to theme.liquid or product.liquid -->
<script type="application/ld+json">
{{ product_schemn }}
</script>
```

Or manually add in the `<head>` section via:
- **Online Store > Themes > Edit Code > product.liquid**
- Add the JSON-LD `<script>` block before `</head>`

**Recommended Apps:**
- JSON-LD for SEO (by Ilana Davis)
- Smart SEO
- Schema Plus for SEO

### WooCommerce
Add via functions.php or a plugin:
```php
function add_product_schema() {
    if (is_product()) {
        // Add your JSON-LD script here
        echo '<script type="application/ld+json">' . $schema_json . '</script>';
    }
}
add_action('wp_head', 'add_product_schema');
```

**Recommended Plugins:**
- Yoast SEO (generates basic schema)
- Rank Math (comprehensive schema support)
- Schema Pro

### Amazon / Mar you cannot add custom schema to standard listings.
brand and key attributes
- Full product description in the A+ content modules
- High-quality product images with proper file names
- Detailed bullet points covering key features
- Brand Registry enrollment for A+ content access

For marketplaces, GEO signals come from content quality, not technical schema.

### Custom / DTC Sites
Add directly in HTML `<head>`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Product",
  ...your schema here...
}
</script>
```

---

## Output Format

Always deliver:

```markdown
## Schema Markup — [Product/Store Name]

### Implementation Instructions
[Platform-specific steps to add the schema]

### 1. Product + Offer + Rating Schema (add to all product pages)

```json
[complete JSON-LD]
```

### 2. FAQ Schema (add if FAQ section exists)

```json
[complete JSON-LD]
```

### 3. Organization Schema (add once to homepage/header)

```json
[complete JSON-LD]
```

### 4. BreadcrumbList Schema (add to product and category pages)

```json
[complete JSON-LD]
```

### Validation
Test your schema at: https://search.google.com/test/rich-results
All errors must be resolved before the schema benefits your GEO score.

### Expected GEO Impact
[Summarize the estimated improvement across GEO pillars after adding this schema]
```

---

## Common Schema Mist ("InStock" not "in stock")

❌ **Multiple `@type: Product` on one page** — Only one Product schema per page

❌ **Escaped HTML in descriptions** — Use plain text, not `&amp;` or `&lt;`

❌ **Missing `@context`** — Every schema block needs `"@context": "https://schema.org/"`

❌ **FAQ answers)
- [ ] Price currency is correct ISO code (USD, GBP, EUR, etc.)
- [ ] Availability uses schema.org URL format
- [ ] FAQ answers are concise and direct
- [ ] Schema matches actual page content (no mismatches)

---

## Skill Workflow Position

```
📐 Schema & Structured Data Flow
├── structured-data-advisor   → Decide which schemas to implement
├── schema-markup-generator   → Generate the schema code ← YOU ARE HERE
├── schema-validator          → Check for errors and completeness
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

- Schema is generated based on information provided — verify against actual page content
- Live validation requires Google Rich Results Test or Schema.org validator
- Amazon and most marketplangs do not support custom schema implementation
- Schema alone does not guarantee AI citations — content quality matters equally
- Schema must be kept updated when product details change (price, availability, reviews)
