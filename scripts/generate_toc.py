#!/usr/bin/env python3
"""
Script to generate a Table of Contents (ToC) from the README.md structure.
Extracts sections and subsections and creates a reference file in data/toc.yml
"""
import re
import json
from pathlib import Path

README_PATH = Path(__file__).parent.parent / "README.md"
TOC_YML_PATH = Path(__file__).parent.parent / "data" / "toc.yml"

def extract_toc_from_readme(readme_text):
    """Extract table of contents structure from README.md."""
    lines = readme_text.split('\n')
    toc_structure = []
    current_section = None
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        
        # Match main sections (##)
        section_match = re.match(r'^## (.+)', line)
        if section_match:
            section_title = section_match.group(1).strip()
            current_section = {
                'title': section_title,
                'subsections': []
            }
            toc_structure.append(current_section)
            continue
        
        # Match subsections (###)
        subsection_match = re.match(r'^### (.+)', line)
        if subsection_match and current_section:
            subsection_title = subsection_match.group(1).strip()
            current_section['subsections'].append({
                'title': subsection_title
            })
    
    return toc_structure

def write_toc_yaml(toc_structure, output_path):
    """Write table of contents to YAML file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Table of Contents for Agentic AI Bibliography\n')
        f.write('# Generated from README.md structure\n')
        f.write('# This file provides a hierarchical overview of the bibliography organization\n\n')
        f.write('toc:\n')
        
        for section in toc_structure:
            f.write('  - title: ' + json.dumps(section['title']) + '\n')
            
            if section['subsections']:
                f.write('    subsections:\n')
                for subsection in section['subsections']:
                    f.write('      - title: ' + json.dumps(subsection['title']) + '\n')
            f.write('\n')

def generate_markdown_toc(toc_structure):
    """Generate a markdown version of the ToC for easy reading."""
    markdown_lines = ['# Table of Contents\n']
    
    for section in toc_structure:
        markdown_lines.append(f"## {section['title']}")
        
        if section['subsections']:
            for subsection in section['subsections']:
                markdown_lines.append(f"  - {subsection['title']}")
        
        markdown_lines.append('')  # Empty line between sections
    
    return '\n'.join(markdown_lines)

def main():
    """Main function to generate ToC files."""
    if not README_PATH.exists():
        print(f"Error: {README_PATH} not found")
        return
    
    print(f"Reading from {README_PATH}")
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    print("Extracting table of contents structure...")
    toc_structure = extract_toc_from_readme(readme_content)
    
    print(f"Found {len(toc_structure)} main sections")
    total_subsections = sum(len(section['subsections']) for section in toc_structure)
    print(f"Found {total_subsections} subsections")
    
    # Create output directory if it doesn't exist
    TOC_YML_PATH.parent.mkdir(exist_ok=True)
    
    print(f"Writing YAML ToC to {TOC_YML_PATH}")
    write_toc_yaml(toc_structure, TOC_YML_PATH)
    
    # Also create a markdown version for easy reading
    toc_md_path = TOC_YML_PATH.with_suffix('.md')
    print(f"Writing Markdown ToC to {toc_md_path}")
    markdown_toc = generate_markdown_toc(toc_structure)
    with open(toc_md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_toc)
    
    print(f"Successfully generated ToC files")
    
    # Print structure for verification
    print("\nTable of Contents Structure:")
    for section in toc_structure:
        print(f"  {section['title']}")
        for subsection in section['subsections']:
            print(f"    - {subsection['title']}")

if __name__ == "__main__":
    main()
