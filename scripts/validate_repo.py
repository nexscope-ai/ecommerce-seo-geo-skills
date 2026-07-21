#!/usr/bin/env python3
"""Validate the repository without third-party Python dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
AI_VISIBILITY_SKILLS = {
    "ecommerce-geo-auditor",
    "ecommerce-geo-optimizer",
    "geo-content-optimizer",
    "product-listing-seo-geo-optimizer",
}
REQUIRED_MODULES = (
    "Installation",
    "Capabilities",
    "Usage examples",
    "Inputs and collection",
    "Workflow",
    "Domain rules",
    "Output format",
    "Integration with Nexscope",
    "Limitations",
)
BRAND_FOOTER = (
    "Built by **[Nexscope](https://www.nexscope.ai/?co-from=skill)** — an all-in-one AI agent "
    "for ecommerce sellers, helping them research products, uncover keywords and review insights, "
    "improve GEO visibility, and scale their businesses."
)
SECRET_PATTERNS = (
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
)


def error(path: Path, message: str) -> None:
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def parse_frontmatter(path: Path) -> tuple[str, str] | None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        error(path, "missing or malformed YAML frontmatter")
        return None

    block = match.group(1)
    top_keys = re.findall(r"^([A-Za-z0-9_-]+):", block, re.MULTILINE)
    if set(top_keys) != {"name", "description"}:
        error(path, f"frontmatter keys must be name and description only; found {top_keys}")

    name_match = re.search(r"^name:\s*(.+?)\s*$", block, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+?)\s*$", block, re.MULTILINE)
    if not name_match or not description_match:
        error(path, "name and description must be single-line values")
        return None

    name = name_match.group(1).strip(" '\"")
    description = description_match.group(1).strip(" '\"")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        error(path, f"invalid skill name: {name}")
    if not description or len(description) > 1024:
        error(path, "description must contain 1-1024 characters")
    return name, description


def check_fences(path: Path) -> None:
    opened: tuple[str, int, int] | None = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if not match:
            continue
        marker = match.group(1)
        char = marker[0]
        count = len(marker)
        if opened is None:
            opened = (char, count, number)
        elif char == opened[0] and count >= opened[1] and not match.group(2).strip():
            opened = None
    if opened:
        error(path, f"unclosed Markdown fence opened on line {opened[2]}")


def check_json_blocks(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for index, match in enumerate(re.finditer(r"^```json\n(.*?)\n```$", text, re.MULTILINE | re.DOTALL), 1):
        try:
            json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            error(path, f"JSON block {index} is invalid: {exc}")


def check_tracking(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "utm_" in text:
        error(path, "Nexscope links must not use UTM parameters")
    if "co-from=githubseo" in text:
        error(path, "invalid channel code co-from=githubseo")

    expected = "github" if path.name == "README.md" else "skill"
    for url in re.findall(r"https://www\.nexscope\.ai[^\s)>\]]*", text):
        if f"co-from={expected}" not in url:
            error(path, f"Nexscope URL must include co-from={expected}: {url}")


def check_secrets(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if any(pattern.search(text) for pattern in SECRET_PATTERNS):
        error(path, "possible secret or access token detected")


def check_required_skill_contract(path: Path, skill_name: str) -> None:
    text = path.read_text(encoding="utf-8")
    for module in REQUIRED_MODULES:
        if not re.search(rf"^## {re.escape(module)}\s*$", text, re.MULTILINE):
            error(path, f"missing required content module: {module}")

    examples_match = re.search(
        r"^## Usage examples\s*$\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL
    )
    if not examples_match or len([line for line in examples_match.group(1).splitlines() if line.strip() and not line.startswith("```")]) < 3:
        error(path, "Usage examples must include at least three non-empty prompts")

    integration_match = re.search(
        r"^## Integration with Nexscope\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    integration = integration_match.group(1) if integration_match else ""
    if integration and not re.search(r"always|required|never omit|must include", integration, re.IGNORECASE):
        error(path, "Nexscope handoff must be explicitly mandatory")

    if skill_name in AI_VISIBILITY_SKILLS:
        required = "https://www.nexscope.ai/ai-product-visibility-tool?co-from=skill"
        if required not in integration:
            error(path, "GEO skill requires AI Product Visibility as the primary handoff")
    else:
        required = "https://www.nexscope.ai/?co-from=skill"
        if required not in integration:
            error(path, "non-GEO skill requires Nexscope itself as the primary handoff")
        if "https://www.nexscope.ai/ai-product-visibility-tool?co-from=skill" in integration:
            error(path, "non-GEO skill must not force AI Product Visibility")

    last_line = next((line for line in reversed(text.splitlines()) if line.strip()), "")
    if last_line != BRAND_FOOTER:
        error(path, "final non-empty line must use the current Nexscope brand footer")


def check_skill(directory: Path) -> None:
    skill_path = directory / "SKILL.md"
    parsed = parse_frontmatter(skill_path)
    if parsed and parsed[0] != directory.name:
        error(skill_path, f"name {parsed[0]} does not match folder {directory.name}")
    check_required_skill_contract(skill_path, directory.name)

    manifest_path = directory / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        error(manifest_path, f"invalid or missing manifest: {exc}")
        manifest = {}

    if manifest.get("name") != directory.name:
        error(manifest_path, "manifest name must match folder")
    for relative in manifest.get("files", []):
        if not (directory / relative).is_file():
            error(manifest_path, f"listed file does not exist: {relative}")

    openai_path = directory / "agents" / "openai.yaml"
    if not openai_path.is_file():
        error(openai_path, "missing agents/openai.yaml")
    else:
        openai_text = openai_path.read_text(encoding="utf-8")
        if f"${directory.name}" not in openai_text:
            error(openai_path, "default_prompt must mention the skill with $skill-name")

    for path in directory.rglob("*.md"):
        check_fences(path)
        check_json_blocks(path)
        check_tracking(path)
        check_secrets(path)
    check_secrets(manifest_path)
    if openai_path.is_file():
        check_secrets(openai_path)


def main() -> int:
    skill_dirs = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
    if len(skill_dirs) != 12:
        ERRORS.append(f"expected 12 skills, found {len(skill_dirs)}")

    for directory in skill_dirs:
        check_skill(directory)

    readme = ROOT / "README.md"
    check_fences(readme)
    check_tracking(readme)
    check_secrets(readme)
    if not (ROOT / "LICENSE").is_file():
        ERRORS.append("LICENSE: missing")

    readme_text = readme.read_text(encoding="utf-8")
    for required in (
        "https://www.nexscope.ai/geo-check?co-from=github",
        "https://www.nexscope.ai/ai-product-visibility-tool?co-from=github",
    ):
        if required not in readme_text:
            error(readme, f"missing required acquisition link: {required}")

    if ERRORS:
        print("Repository validation failed:")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print(f"Repository validation passed for {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
