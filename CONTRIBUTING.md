# Contributing to Agentic AI Bibliography

Thank you for your interest in contributing!

This repository is a curated, evolving bibliography intended to help builders,
researchers, and teams navigate the emerging field of **Agentic AI**. To
maintain clarity, quality, and usefulness, we ask that all contributions follow
the guidelines below.

## 🚀 How Our Automated System Works

This repository uses an **automated pipeline** to maintain consistency and
quality:

- **Main Data Source**: All bibliography entries are stored in
  `data/bib.yml` in structured YAML format
- **Auto-Generation**: Markdown files in `bibliography/` are automatically
  generated from the YAML data
- **Quality Assurance**: All generated content passes markdownlint validation
- **Continuous Integration**: GitHub Actions automatically validate changes
  and regenerate files

**Important**: The markdown files in `bibliography/` are auto-generated.
Direct edits to these files will be overwritten. Always edit `data/bib.yml`.

## 📚 What You Can Contribute

- New references (papers, books, tools, videos, benchmarks, etc.)
- Improvements to existing entries (typos, summaries, updated links)
- Suggestions for section structure or new thematic areas
- Additional metadata (authors, publication year, access links)

## 📝 How to Add a New Entry

All entries must be added to `data/bib.yml`. For reference, see the complete
template at `template/bibliography_entry_template.yml`. Each entry follows
this structure:

```yaml
- id: "unique-identifier"
  title: "Paper or Resource Title"
  authors: "Author Name(s)"
  year: 2024
  section: "section"  # Must match existing section
  subsection: "subsection"  # Must match existing section
  description: |
    A 3–5 line summary describing what the resource contributes to the
    understanding or implementation of Agentic AI. Keep the tone neutral
    and informative. Focus on insights, methods, or practical applications.
  cross_references:  # Optional: if referenced in multiple sections
    - section: "secondary subsection"  # Must match existing section
      subsection: "secondary subsection"  # Must match existing section
      context: "Referenced as implementation example"
  links:
    internal: "./papers/filename.pdf"  # Optional: local repo PDF
    external: "https://arxiv.org/abs/2024.12345"  # Official source
    code: "https://github.com/author/project"  # Optional: code repository
```

### Required Fields

- `id`: Unique identifier (use author-title format, e.g., "smith-ai-agents")
- `title`: Full title of the resource
- `authors`: Author name(s) in "LastName et al." format for multiple authors
- `year`: Publication year (integer)
- `section`: Must be one of the existing sections (see below)
- `description`: 3-5 line summary in neutral, informative tone

### Optional Fields

- `cross_references`: List of other sections where this work is mentioned
- `links.internal`: Path to PDF in `papers/` folder (only for open-access)
- `links.external`: Official source URL
- `links.code`: Code repository URL

For complete field descriptions and examples, see
`template/bibliography_entry_template.yml`.

## 🧭 Available Sections

Entries must be assigned to one of these existing sections:

1. **foundational-concepts**  
2. **architectures-and-system-design**  
3. **evaluation-and-benchmarks**  
4. **tools-and-frameworks**  
5. **operating-agents-in-production-agentops**  
6. **simulation-frameworks-and-experimental-agent-environments**  
7. **case-studies-and-applications**  
8. **critical-perspectives-and-futures**  
9. **industry-vision-and-strategic-perspectives**

If you're unsure where your entry belongs, suggest a location in your pull
request.

## ⚖️ Licensing and Intellectual Property

Please respect intellectual property rights.

- Do **not** upload full books, articles, or content that is under copyright
  and not licensed for redistribution.
- You **may** upload open-access papers (e.g., from arXiv or official public
  sources) to the `/papers/` folder.
- When in doubt, **link to the source** rather than hosting the file.
- We aim to support fair use and academic sharing, but not to infringe on the
  rights of authors or publishers.

By contributing, you confirm that any resource you add is either:

- Freely and legally redistributable, **or**
- Only linked to via a public, official, or publisher-approved source.

## 🌍 Language and Tone Guidelines

- Write in English
- Keep summaries concise, neutral, and informative
- Avoid promotional language
- Focus on what the resource adds to the understanding or practice of Agentic AI
- Use consistent formatting and punctuation

## 🔁 Contribution Process

1. **Fork the repository**
2. **Create a branch** for your contribution
3. **Edit `data/bib.yml`** following the format above
4. **Add PDFs** (if applicable) to the `papers/` folder
5. **Test locally** (optional but recommended):

   ```bash
   cd scripts/
   python build.py
   ```

6. **Open a pull request** with a description of your changes
7. **Automated validation** will check your contribution
8. **Review and merge** by maintainers

## 🤖 Automated Validation

All pull requests automatically run:

- **Consistency checks** on YAML structure and references
- **Markdownlint validation** on generated files
- **Preview generation** of updated bibliography sections

You'll see results in the PR checks. Fix any issues before requesting review.

## 🤝 Thank You

Your contributions help keep this bibliography useful, relevant, and grounded.
Let's build a shared foundation of thoughtful, high-quality knowledge in the
age of agents.
