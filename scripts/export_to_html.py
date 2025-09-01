#!/usr/bin/env python3
"""
Export bibliography from YAML to HTML files instead of markdown.
This bypasses Jekyll issues and creates static HTML directly.
"""

import re
import yaml  # type: ignore
from pathlib import Path
from typing import Dict, Any


def create_html_template(title: str, content: str) -> str:
    """Create a complete HTML page with the given title and content."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Agentic AI Bibliography</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
        }}
        h1 {{
            color: #0366d6;
            border-bottom: 3px solid #e1e4e8;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        h2 {{
            color: #0366d6;
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        .entry {{
            margin: 20px 0;
            padding: 15px;
            background: #f6f8fa;
            border-radius: 6px;
            border-left: 4px solid #0366d6;
        }}
        .entry-title {{
            font-weight: 600;
            color: #0366d6;
            margin-bottom: 5px;
        }}
        .entry-summary {{
            margin: 10px 0;
            color: #586069;
        }}
        .links {{
            margin-top: 10px;
        }}
        .links a {{
            display: inline-block;
            margin-right: 15px;
            color: #0366d6;
            text-decoration: none;
            border: 1px solid #0366d6;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.9em;
        }}
        .links a:hover {{
            background: #0366d6;
            color: white;
        }}
        .nav {{
            background: #f6f8fa;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 30px;
        }}
        .nav a {{
            color: #0366d6;
            text-decoration: none;
            margin-right: 20px;
        }}
        .nav a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="nav">
        <a href="../index.html">← Home</a>
        <a href="README.html">Bibliography Index</a>
    </div>
    <h1>{title}</h1>
    {content}
</body>
</html>"""


def format_entry_html(entry: Dict[str, Any]) -> str:
    """Format a single bibliography entry as HTML."""
    title = entry.get('title', 'Untitled')
    author = entry.get('author', 'Unknown Author')
    year = entry.get('year', 'Unknown Year')
    summary = entry.get('summary', '')
    links = entry.get('links', [])
    
    html = f'<div class="entry">'
    html += f'<div class="entry-title">{author} – <em>{title}</em> ({year})</div>'
    
    if summary:
        html += f'<div class="entry-summary">{summary}</div>'
    
    if links:
        html += '<div class="links">'
        for link in links:
            link_text = link.get('text', 'Link')
            link_url = link.get('url', '#')
            if link_url.startswith('./papers/'):
                link_url = '../' + link_url[2:]  # Adjust relative path
            html += f'<a href="{link_url}">{link_text}</a>'
        html += '</div>'
    
    html += '</div>'
    return html


def export_to_html():
    """Export bibliography to HTML files."""
    # Read the YAML data
    data_file = Path('data/bib.yml')
    with open(data_file, 'r', encoding='utf-8') as f:
        entries = yaml.safe_load(f)
    
    # Group by section
    sections = {}
    for entry in entries:
        section = entry.get('section', 'Other')
        if section not in sections:
            sections[section] = []
        sections[section].append(entry)
    
    # Create output directory
    output_dir = Path('bibliography')
    output_dir.mkdir(exist_ok=True)
    
    # Generate each section
    for section_title, section_entries in sections.items():
        # Create safe filename
        safe_filename = re.sub(r'[^a-zA-Z0-9\s-]', '', section_title.lower())
        safe_filename = re.sub(r'\s+', '-', safe_filename)
        html_file = output_dir / f"{safe_filename}.html"
        
        # Generate content
        content = ""
        if section_entries:
            for entry in sorted(section_entries, key=lambda x: (x.get('year', 0), x.get('author', ''))):
                content += format_entry_html(entry)
        
        # Write HTML file
        html_content = create_html_template(section_title, content)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {html_file}")
    
    print("HTML generation completed!")


if __name__ == "__main__":
    export_to_html()
