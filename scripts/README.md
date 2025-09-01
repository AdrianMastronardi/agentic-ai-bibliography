# Scripts Documentation

This directory contains automation scripts for the Agentic AI Bibliography project.

## Overview

The bibliography system converts entries from `README.md` to structured YAML
format, then exports to markdown:

1. **Export**: `data/bib.yml` → `bibliography/*.md` files
2. **Validation**: Consistency checks between files

*Note: Initial migration from README.md has been completed.*

## Main Scripts

### `build.py` - Main Build Script

Orchestrates the complete build process:

```bash
python scripts/build.py
```

Runs in sequence:

1. Consistency checks
2. Markdown export

### `export_to_bibliography.py` - Bibliography Export

Creates individual markdown files from YAML data:

```bash
python scripts/export_to_bibliography.py
```

Generates:

- `bibliography/README.md` - Index of all sections
- `bibliography/{number}-{section}.md` - Individual numbered section files
- Uses README.md citation format
- Proper link formatting and cross-references

### `check_consistency_simple.py` - Validation

Validates consistency between YAML files:

```bash
python scripts/check_consistency_simple.py
```

Checks:

- All sections in bib.yml exist in toc.yml
- All subsections in bib.yml exist in toc.yml
- Reports unused sections (warnings)

## Dependencies

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## File Structure

```text
scripts/
├── build.py                        # Main orchestration script
├── export_to_bibliography.py        # YAML → Bibliography markdown export
├── check_consistency_simple.py     # Validation and consistency checks
└── README.md                       # This documentation
```

## Output Structure

After running the build process:

```text
data/
├── bib.yml                         # Bibliography entries
└── toc.yml                         # Table of contents structure

bibliography/
├── README.md                       # Section index
├── 1-foundational-concepts.md      # Individual numbered section files
├── 2-architectures-and-system-design.md
└── ...                            # One file per section
```

## GitHub Actions

The project includes automated CI/CD via `.github/workflows/build.yml`:

- **Triggers**: Push to main/refactor branches, PRs, manual dispatch
- **Validation**: YAML structure, required fields, duplicate IDs
- **Build**: Consistency checks, markdown export
- **Artifacts**: Uploads markdown files
- **Deploy**: Publishes to GitHub Pages (main branch only)

## Cross-Platform Notes

- Scripts use cross-platform paths (`pathlib`)
- Unicode handling for Windows compatibility
- Emoji-free output for terminal compatibility
- Virtual environment support
