#!/usr/bin/env python3
"""
Export bibliography from YAML to individual markdown files in
bibliography/ directory.
Uses the same citation format as README.md.
"""

import re
import yaml  # type: ignore
from pathlib import Path
from typing import Dict, Any


def _format_internal_pdf_link(entry_id: str) -> str:
    """Format internal PDF link."""
    return f"[Read the full paper from this repo](../papers/{entry_id}.pdf)"


def _format_source_link(url: str) -> str:
    """Format source link based on URL type."""
    if 'arxiv.org' in url:
        return f"[Read the full paper from the source]({url})"
    elif 'github.com' in url:
        return f"[Explore the repository]({url})"
    elif 'youtube.com' in url or 'youtu.be' in url:
        return f"[Watch the full talk]({url})"
    else:
        return f"[Access the source]({url})"


def fix_cross_references(url: str) -> str:
    """Convert internal fragment links to proper file references."""
    if url.startswith('#'):
        # Map fragment IDs to file names
        fragment_to_file = {
            '#3-evaluation-and-benchmarks': '3-evaluation-and-benchmarks.md',
            '#4-tools-and-frameworks': '4-tools-and-frameworks.md',
            '#5-operating-agents': (
                '5-operating-agents-in-production-agentops.md'
            ),
            '#6-simulation-frameworks': (
                '6-simulation-frameworks-and-experimental-agent-'
                'environments.md'
            ),
            '#7-case-studies': '7-case-studies-and-applications.md',
            '#8-critical-perspectives': (
                '8-critical-perspectives-and-futures.md'
            ),
            '#9-industry-vision': (
                '9-industry-vision-and-strategic-perspectives.md'
            )
        }
        return fragment_to_file.get(url, url)
    return url


def _format_single_link(link: Dict[str, Any], entry_id: str) -> str:
    """Format a single link based on its type."""
    link_type = link.get('type', 'unknown')
    url = link.get('url', '')

    # Fix cross-references for fragment links
    if url:
        url = fix_cross_references(url)

    if link_type == 'internal_pdf':
        return _format_internal_pdf_link(entry_id)
    elif link_type == 'source':
        if url:
            return _format_source_link(url)
        else:
            return "[Source (URL not available)]"
    elif link_type == 'repo':
        if url:
            return f"[Explore the code repository]({url})"
        else:
            return "[Repository (URL not available)]"
    else:
        text = link_type.title()
        return f"[{text}]({url})" if url else f"[{text}]"


def sanitize_filename(text: str) -> str:
    """Convert section title to safe filename with section number."""
    # Extract section number if present
    section_match = re.match(r'^(\d+)\.\s*(.+)', text)
    if section_match:
        section_num = section_match.group(1)
        section_name = section_match.group(2)
    else:
        section_num = ""
        section_name = text

    # Clean up the section name
    clean_name = re.sub(r'[^\w\s-]', '', section_name)
    clean_name = re.sub(r'[-\s]+', '-', clean_name)
    clean_name = clean_name.lower().strip('-')

    # Combine number and name
    if section_num:
        return f"{section_num}-{clean_name}"
    else:
        return clean_name


def format_authors(author: str) -> str:
    """Format author names for display."""
    if not author:
        return "Unknown Author"

    # Handle "et al." cases
    if "et al." in author:
        return author

    # Handle multiple authors separated by various delimiters
    authors = re.split(r',\s*|\s+&\s+|\s+and\s+', author)
    if len(authors) > 3:
        return f"{authors[0]} et al."
    elif len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    else:
        return author


def format_links_readme_style(entry: Dict[str, Any]) -> str:
    """Format links in README.md style."""
    if 'links' not in entry or not entry['links']:
        return ""

    links = []
    entry_id = entry.get('id', '')

    for link in entry['links']:
        formatted_link = _format_single_link(link, entry_id)
        links.append(formatted_link)

    # Add arXiv link if available
    arxiv = entry.get('arxiv', '')
    if arxiv:
        arxiv_link = (f"[Read the full paper from the source]"
                      f"(https://arxiv.org/abs/{arxiv})")
        links.append(arxiv_link)

    if links:
        return " · ".join(links)
    return ""


def clean_multiple_blank_lines(content: str) -> str:
    """Remove multiple consecutive blank lines, keeping only single blanks."""
    import re
    # Replace multiple consecutive newlines with maximum of 2 (one blank line)
    # First normalize all whitespace-only lines to empty lines
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    # Then remove multiple consecutive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Ensure file doesn't end with multiple blank lines
    content = content.rstrip('\n') + '\n'
    return content


def wrap_text(text: str, width: int = 80, indent: str = "") -> str:
    """Wrap text to specified width with proper indentation."""
    import textwrap

    # Use textwrap to handle the wrapping
    wrapped = textwrap.fill(
        text,
        width=width,
        initial_indent=indent,
        subsequent_indent=indent,
        break_long_words=False,
        break_on_hyphens=False
    )
    return wrapped


def format_entry_citation(entry: Dict[str, Any]) -> str:
    """Format a single bibliography entry in README.md citation style."""
    title = entry.get('title', 'Untitled')
    author = format_authors(entry.get('author', ''))
    year = entry.get('year', 'Unknown')
    summary = entry.get('summary', 'No summary available.')

    # Format the citation line with proper wrapping
    citation_text = f"**{author} – *{title}* ({year})**"
    citation = wrap_text(citation_text, width=78, indent="- ")

    # Add summary with proper indentation and wrapping
    formatted_summary = []
    summary_lines = summary.split('\n')
    for line in summary_lines:
        if line.strip():
            wrapped_line = wrap_text(line.strip(), width=78, indent="  ")
            formatted_summary.append(wrapped_line)

    # Add links if available
    links = format_links_readme_style(entry)
    if links:
        wrapped_links = wrap_text(links, width=78, indent="  ")
        formatted_summary.append(wrapped_links)

    # Combine citation and summary with proper spacing
    result_parts = [citation]
    if formatted_summary:
        result_parts.extend(formatted_summary)

    # Add blank line after entry for proper spacing
    return "\n".join(result_parts) + "\n\n"


def load_toc_descriptions() -> Dict[str, str]:
    """Load section descriptions from toc.yml."""
    toc_path = Path(__file__).parent.parent / "data" / "toc.yml"
    descriptions = {}

    try:
        with open(toc_path, 'r', encoding='utf-8') as f:
            toc_data = yaml.safe_load(f)

        for section in toc_data.get('toc', []):
            title = section.get('title', '')
            description = section.get('description', '')
            if title and description:
                descriptions[title] = description.strip()

    except Exception as e:
        print(f"Warning: Could not load ToC descriptions: {e}")

    return descriptions


def export_to_bibliography():
    """Main export function."""
    # Set up paths
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    output_dir = script_dir.parent / "bibliography"
    bib_file = data_dir / "bib.yml"

    print(f"Reading bibliography from {bib_file}")

    # Load bibliography data
    try:
        with open(bib_file, 'r', encoding='utf-8') as f:
            entries = yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading bibliography: {e}")
        return

    # Load ToC descriptions
    toc_descriptions = load_toc_descriptions()

    # Group entries by section
    sections = {}
    subsection_counts = {}

    for entry in entries:
        section = entry.get('section', 'Uncategorized')
        if section not in sections:
            sections[section] = []
        sections[section].append(entry)

        # Count subsections
        subsection = entry.get('subsection', '')
        if subsection:
            if section not in subsection_counts:
                subsection_counts[section] = set()
            subsection_counts[section].add(subsection)

    # Create output directory
    output_dir.mkdir(exist_ok=True)
    print(f"Creating markdown files in {output_dir}")

    # Export each section
    section_files = []
    for section_title, section_entries in sections.items():
        # Create safe filename
        section_filename = sanitize_filename(section_title) + ".md"
        section_file = output_dir / section_filename

        # Build content first, then clean it
        content_parts = []

        # Write header
        content_parts.append(f"# {section_title}\n\n")

        # Add description if available
        if section_title in toc_descriptions:
            description = toc_descriptions[section_title]
            wrapped_desc = wrap_text(description, width=80)
            content_parts.append(wrapped_desc + "\n\n")

        # Group by subsection
        subsections = {}
        no_subsection = []

        for entry in section_entries:
            subsection = entry.get('subsection', '')
            if subsection:
                if subsection not in subsections:
                    subsections[subsection] = []
                subsections[subsection].append(entry)
            else:
                no_subsection.append(entry)

        # Sort entries by year within each group
        no_subsection.sort(
            key=lambda x: (x.get('year', 0), x.get('author', ''))
        )

        # Write entries without subsections first
        for entry in no_subsection:
            content_parts.append(format_entry_citation(entry))

        # Write subsections
        for subsection_title, subsection_entries in sorted(
            subsections.items()
        ):
            # Add blank line before subsection header
            content_parts.append(f"\n## {subsection_title}\n\n")

            # Sort entries by year within subsection
            subsection_entries.sort(
                key=lambda x: (x.get('year', 0), x.get('author', ''))
            )

            for entry in subsection_entries:
                content_parts.append(format_entry_citation(entry))

        # Join all content and clean multiple blank lines
        full_content = "".join(content_parts)
        clean_content = clean_multiple_blank_lines(full_content)

        # Write the cleaned content to file
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(clean_content)

        section_files.append((
            section_title, section_filename, len(section_entries)
        ))
        print(f"Created {section_file} with {len(section_entries)} entries")

    # Create main README file
    readme_file = output_dir / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write("# Agentic AI Bibliography\n\n")

        # Wrap the description properly
        description = ("This directory contains the bibliography organized by "
                       "sections. Each section is available as an individual "
                       "markdown file.")
        wrapped_desc = wrap_text(description, width=80)
        f.write(wrapped_desc + "\n\n")

        f.write("## Sections\n\n")

        for section_title, filename, entry_count in section_files:
            # Wrap long section titles if needed
            entry_text = (f"[{section_title}]({filename}) "
                          f"({entry_count} entries)")
            if len(entry_text) > 76:  # Account for "- " prefix
                wrapped_entry = wrap_text(entry_text, width=78, indent="- ")
            else:
                wrapped_entry = f"- {entry_text}"
            f.write(wrapped_entry + "\n")

        f.write(f"\n**Total Entries:** {len(entries)}\n\n")
        f.write("**Last Updated:** Generated from bibliography data\n\n")
        f.write("---\n\n")

        # Format repository link properly to avoid bare URL warning
        f.write("**Repository:** ")
        repo_url = ("https://github.com/AdrianMastronardi/"
                    "agentic-ai-bibliography")
        f.write(f"<{repo_url}>\n")

    print(f"Created main README file {readme_file}")
    export_msg = (f"Export completed! Generated {len(section_files)} "
                  f"section files with {len(entries)} total entries.")
    print(export_msg)


if __name__ == "__main__":
    export_to_bibliography()
