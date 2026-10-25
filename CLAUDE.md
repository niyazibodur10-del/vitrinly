# Vitrinly — project instructions

The user (Niyazi) is the owner and makes the product decisions together with you. Speak Turkish.
Nutrigold is archived in `~/.claude/nutrigold/` (its old CLAUDE.md is `CLAUDE-nutrigold.md`, its agents are in `agents/`). Do not use it unless Niyazi asks.

## The product
An AI-based web panel (SaaS) for e-commerce sellers. Start: **Trendyol + Hepsiburada**; global marketplaces later.
Modules, all in one panel:
1. **SEO title & description writer**: knows each marketplace's current ranking factors and listing rules; writes search-optimised, rule-compliant titles and descriptions.
2. **Compliance shield**: checks texts against marketplace rules, Reklam Kurulu / advertising law and category claim rules; rewrites them to comply.
3. **Image generation**: Claude writes the image prompts from our rule set (marketplace image rules + compliance); an image model (OpenAI) renders them. Target: 4 images per product per day.
4. **Customer question & review replies**.
5. **Profitability analysis** (later, after the marketplace integrations).

Architecture rule: **every customer request first goes to the central AI coordinator**, which routes it to the right module/agent and to the external platforms (Trendyol, Hepsiburada, OpenAI), then merges the result.

## Decisions so far
- Team: Claude + the agents below. No outside developers.
- Phase 0 validation (landing + waitlist + seller interviews) → MVP → integrations → profitability.
- Image pipeline is **provider-agnostic** (not tied to OpenAI): real seller photo → background removal (open-source, own server) → AI scene edit via an edit model (candidates: Qwen Image Edit, FLUX Kontext/FLUX.2 via fal.ai or Cloudflare Workers AI) → text/infographics rendered by our own code (AI models garble Turkish text). Pick the model by a blind quality test. No usable free API tier exists for production volume (OpenAI none; Gemini image API paid-only per late-2026 snippets; Cloudflare 10k neurons/day ≈ a handful of images, fine for testing). Image costs go into plans as credits.
- Niyazi's subscriptions: **Google AI Pro** (includes ~$10/month Google Cloud credit usable on the Gemini API → Gemini image model joins the blind test and covers early volume; must be activated via Google Developer Program, credits expire), **Photoroom Pro** and **Canva Pro** (app subscriptions, no SaaS API rights: Photoroom API is billed separately, Canva Autofill API needs Enterprise) → use them for benchmarks, template design and our own marketing, not as the customer-facing engine.

## Team (in ~/.claude/agents)
- Software: frontend-developer, backend-architect, code-reviewer, architect-review, debugger, test-automator, security-auditor, performance-engineer, typescript-pro, python-pro, playwright-pro.
- Design: ui-designer, design-system-architect, accessibility-expert, design-ux-architect, design-visual-storyteller, design-image-prompt-engineer.
- Skills: frontend-design, canvas-design, theme-factory, visual-design-foundations, design-system-patterns, responsive-design, tailwind-design-system, nextjs-app-router-patterns; plus the marketing/product/commercial plugin skills.

## How we work
- Niyazi's requests come to you first; you split them, hand them to the right agents in parallel, merge the results and report.
- Recommend, don't list options. Never invent numbers: separate verified facts (with source), search snippets and estimates.
- **Spending money, publishing, deploying to production, contacting sellers/customers and irreversible steps only with Niyazi's approval.**
- Code lives in a GitHub repo; commit and push work so nothing is lost when the container is reclaimed.
