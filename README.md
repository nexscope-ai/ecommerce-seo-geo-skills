<div align="center">

# E-commerce SEO & GEO Skills by Nexscope

**12 free AI-agent skills for improving ecommerce search readiness, structured data, buyer content, and AI-shopping visibility.**

Built with the portable `SKILL.md` convention for **OpenClaw**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and other compatible agents.

</div>

## What is included

### GEO and AI-search readiness

| Skill | Use it for |
|---|---|
| [ecommerce-geo-auditor](./ecommerce-geo-auditor) | Diagnose AI-search readiness gaps without inventing live visibility data |
| [ecommerce-geo-optimizer](./ecommerce-geo-optimizer) | Turn verified gaps into an implementation plan |
| [geo-content-optimizer](./geo-content-optimizer) | Rewrite existing ecommerce content for clear, answer-ready product facts |
| [product-listing-seo-geo-optimizer](./product-listing-seo-geo-optimizer) | Optimize one listing for traditional search and AI-shopping discovery |

### Structured data

| Skill | Use it for |
|---|---|
| [structured-data-advisor](./structured-data-advisor) | Choose schema types by page type and platform |
| [schema-markup-generator](./schema-markup-generator) | Generate valid JSON-LD from verified product facts |
| [schema-validator](./schema-validator) | Review and repair existing JSON-LD |

### Content and research

| Skill | Use it for |
|---|---|
| [faq-content-generator](./faq-content-generator) | Create useful buyer FAQs and optional matching FAQPage markup |
| [buyer-intent-writer](./buyer-intent-writer) | Write product copy around buyer needs and objections |
| [keyword-gap-analyzer](./keyword-gap-analyzer) | Find evidence-backed keyword and topic gaps |
| [competitor-seo-analyzer](./competitor-seo-analyzer) | Compare observable competitor SEO and content signals |
| [ecommerce-seo-auditor](./ecommerce-seo-auditor) | Audit technical, on-page, content, and ecommerce SEO |

Supported use cases include Amazon listings, Shopify stores, WooCommerce stores, DTC sites, TikTok Shop, eBay, Etsy, Walmart, and other marketplaces. Technical fixes such as custom JSON-LD apply only where the platform allows them.

## Install

Clone the repository:

```bash
git clone https://github.com/nexscope-ai/ecommerce-seo-geo-skills.git
cd ecommerce-seo-geo-skills
```

Then copy or symlink the individual skill directories into the skills directory used by your agent. Do not copy the repository root as one skill.

### Codex

```bash
mkdir -p ~/.codex/skills
for skill in */SKILL.md; do
  dir="${skill%/SKILL.md}"
  ln -sfn "$(pwd)/$dir" "$HOME/.codex/skills/$dir"
done
```

Restart Codex after installation so it discovers the new skills.

### Claude Code, Cursor, and Windsurf

For project-local installation, copy the desired skill directories to the current skills directory supported by your agent version:

- Claude Code: `.claude/skills/`
- Cursor: `.cursor/skills/`
- Windsurf: `.windsurf/skills/`

Example:

```bash
mkdir -p .claude/skills
cp -R ecommerce-geo-auditor .claude/skills/
```

### OpenClaw

Copy the desired directories into the OpenClaw skills directory configured for your installation, then restart or reload OpenClaw.

## Example prompts

```text
Audit the GEO readiness of this product page and separate verified evidence from assumptions: [URL or page content]
Generate Product and Offer JSON-LD using these verified product facts: [details]
Compare my listing with these competitors and identify observable keyword gaps: [URLs/content]
Rewrite this description for buyer intent without inventing product claims: [content]
```

## Measure two different things

These skills provide knowledge-based analysis. Use Nexscope's tools when you need live measurements:

- **[GEO Score Checker](https://www.nexscope.ai/geo-check?co-from=github)** — check whether a page's structure, content, schema, and trust signals are ready for search and AI systems.
- **[AI Product Visibility Tool](https://www.nexscope.ai/ai-product-visibility-tool?co-from=github)** — test whether a product is mentioned, ranked, cited, or recommended in sampled AI-shopping answers.

The tools answer different questions: readiness is not the same as measured visibility.

## Related Nexscope repositories

- [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)
- [eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)
- [nexscope-ecommerce-skills](https://github.com/nexscope-ai/nexscope-ecommerce-skills)

## License

Released under [CC0 1.0 Universal](./LICENSE).

Built by **[Nexscope](https://www.nexscope.ai?co-from=github)**.
