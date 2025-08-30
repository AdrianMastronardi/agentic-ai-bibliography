#!/usr/bin/env python3
"""
Script to migrate bibliographic entries from README.md to bib.yml format.
                # Join summary and clean up
                summary = ' '.join(summary_parts)
                # Remove link markdown from summary but keep the text content
                summary = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', summary)
                # Clean up any remaining link separators
                summary = re.sub(r'\s*·\s*', ' ', summary)
                summary = re.sub(r'\s+', ' ', summary).strip()rses README.md for each entry (author, title, year, summary, links)
- Outputs YAML entries as in bib/bib.yml
"""
import re
import json
from pathlib import Path

README_PATH = Path(__file__).parent.parent / "README.md"
BIB_YML_PATH = Path(__file__).parent.parent / "data" / "bib.yml"
TOC_YML_PATH = Path(__file__).parent.parent / "data" / "toc.yml"

def generate_toc(readme_text):
    """Generate table of contents structure from README.md."""
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
            
            # Look for description in the next few lines
            description_lines = []
            for i in range(line_num, min(line_num + 10, len(lines))):  # Look ahead up to 10 lines
                next_line = lines[i].strip()
                
                # Stop if we hit another section, subsection, or entry
                if (next_line.startswith('##') or 
                    next_line.startswith('###') or 
                    next_line.startswith('- **')):
                    break
                
                # Collect non-empty lines that look like description content
                if next_line and not next_line.startswith('#'):
                    description_lines.append(next_line)
            
            # Join description and clean it up
            if description_lines:
                description = ' '.join(description_lines)
                # Remove any markdown links but keep the text
                description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', description)
                current_section['description'] = description.strip()
            
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
            
            # Add description if it exists
            if 'description' in section and section['description']:
                f.write('    description: >\n')
                # Write description with proper indentation, splitting long lines
                description = section['description']
                words = description.split()
                line_length = 0
                current_line = []
                
                for word in words:
                    if line_length + len(word) + 1 > 80:  # Wrap at ~80 characters
                        if current_line:
                            f.write('      ' + ' '.join(current_line) + '\n')
                            current_line = [word]
                            line_length = len(word)
                        else:
                            f.write('      ' + word + '\n')
                            line_length = 0
                    else:
                        current_line.append(word)
                        line_length += len(word) + (1 if current_line else 0)
                
                if current_line:
                    f.write('      ' + ' '.join(current_line) + '\n')
            
            if section['subsections']:
                f.write('    subsections:\n')
                for subsection in section['subsections']:
                    f.write('      - title: ' + json.dumps(subsection['title']) + '\n')
            f.write('\n')

def detect_cross_references(readme_text):
    """Detect cross-reference patterns in README.md."""
    cross_refs = {}
    lines = readme_text.split('\n')
    
    current_section = None
    current_subsection = None
    
    for line in lines:
        line = line.strip()
        
        # Track section headers
        section_match = re.match(r'^## (.+)', line)
        subsection_match = re.match(r'^### (.+)', line)
        
        if section_match:
            current_section = section_match.group(1).strip()
            current_subsection = None
        elif subsection_match:
            current_subsection = subsection_match.group(1).strip()
        
        # Look for cross-reference patterns
        # Pattern: "- **TITLE**" followed by "Originally introduced in [Section X](#link), TITLE demonstrates..."
        # Pattern: "- **TITLE**" followed by "Originally covered in [Section X](#link), TITLE..."
        
        # Check if this is a short reference entry (just title in bold, no year)
        short_entry_match = re.match(r'^- \*\*([^*]+)\*\*\s*$', line)
        if short_entry_match:
            title_key = short_entry_match.group(1).strip()
            
            # Look for the next line(s) that might contain cross-reference info
            next_line_idx = lines.index(line) + 1
            if next_line_idx < len(lines):
                next_line = lines[next_line_idx].strip()
                
                cross_ref_patterns = [
                    r'Originally introduced in \[([^\]]+)\]\([^)]+\), (.+)',
                    r'Originally covered in \[([^\]]+)\]\([^)]+\), (.+)'
                ]
                
                for pattern in cross_ref_patterns:
                    match = re.search(pattern, next_line)
                    if match:
                        original_section = match.group(1).strip()
                        context_text = match.group(2).strip()
                        
                        if title_key not in cross_refs:
                            cross_refs[title_key] = []
                        
                        cross_refs[title_key].append({
                            'section': current_section,
                            'subsection': current_subsection,
                            'original_section': original_section,
                            'context': context_text
                        })
    
    return cross_refs

def apply_cross_references(entries, cross_refs):
    """Apply cross-references to entries based on detected patterns."""
    for entry in entries:
        title = entry['title']
        
        # Check if this title has cross-references by matching against cross_ref keys
        for cross_ref_key, cross_ref_list in cross_refs.items():
            # Match by title similarity (exact match, contains, or starts with)
            if (cross_ref_key.lower() == title.lower() or 
                cross_ref_key.lower() in title.lower() or 
                title.lower().startswith(cross_ref_key.lower())):
                
                # This entry has cross-references
                if 'cross_references' not in entry:
                    entry['cross_references'] = []
                
                for cross_ref in cross_ref_list:
                    entry['cross_references'].append({
                        'section': cross_ref['section'],
                        'subsection': cross_ref['subsection'],
                        'context': cross_ref['context']
                    })
                
                print(f"  Applied cross-reference for '{title}' -> '{cross_ref['section']}'")
    
    return entries

def parse_entries(readme_text):
    """Parse bibliographic entries from README.md format."""
    entries = []
    
    # First, let's split the text into lines for better control
    lines = readme_text.split('\n')
    
    # Track current section and subsection
    current_section = None
    current_subsection = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        section_match = re.match(r'^## (.+)', line)
        subsection_match = re.match(r'^### (.+)', line)
        
        if section_match:
            current_section = section_match.group(1).strip()
            current_subsection = None  # Reset subsection when new section starts
            i += 1
            continue
        elif subsection_match:
            current_subsection = subsection_match.group(1).strip()
            i += 1
            continue
        
        # Look for entry start pattern: - **Author – *Title* (Year)**
        entry_match = re.match(r'^- \*\*(.+?) – \*(.+?)\* \((\d{4})\)\*\*\s*$', line)
        
        if entry_match:
            author = entry_match.group(1).strip()
            title = entry_match.group(2).strip()
            year = int(entry_match.group(3))
            
            # Collect content until next entry, section, or end
            content_lines = []
            i += 1
            
            while i < len(lines):
                current_line = lines[i]
                
                # Stop if we hit another entry, section header, or empty line followed by entry/section
                if (current_line.strip().startswith('- **') or 
                    current_line.strip().startswith('##') or 
                    current_line.strip().startswith('###')):
                    break
                
                # Skip empty lines at the start but collect them if they're in the middle
                if current_line.strip() or content_lines:
                    content_lines.append(current_line)
                
                i += 1
            
            # Process the collected content
            content = '\n'.join(content_lines).strip()
            
            if content:  # Only process if we have content
                # Split content into summary and links
                summary_parts = []
                links = []
                
                # Split content into lines and process each
                content_lines_clean = content.split('\n')
                
                for line in content_lines_clean:
                    line = line.strip()  # Remove leading/trailing whitespace including indentation
                    if not line:
                        continue
                        
                    if '[' in line and '](' in line:
                        # Check if this is primarily a links line or content with some links
                        # Calculate text vs links ratio
                        links_text_length = 0
                        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
                        links_found = list(link_pattern.finditer(line))
                        
                        for link_match in links_found:
                            links_text_length += len(link_match.group(0))
                        
                        content_text_length = len(line) - links_text_length
                        
                        # If content text is longer than links text, treat as content with links
                        if content_text_length > links_text_length:
                            # This is content with some links at the end
                            # For summary, extract only the non-link part
                            summary_text = line
                            for link_match in reversed(links_found):  # Remove from end to start
                                summary_text = summary_text[:link_match.start()] + summary_text[link_match.end():]
                            # Clean up any separators
                            summary_text = re.sub(r'\s*·\s*$', '', summary_text).strip()
                            summary_parts.append(summary_text)
                            
                            # Extract links for the links section too
                            for link_match in links_found:
                                link_text = link_match.group(1).strip()
                                link_url = link_match.group(2).strip()
                                
                                # Categorize link type based on URL
                                if link_url.startswith('./papers/') and link_url.endswith('.pdf'):
                                    link_type = 'internal_pdf'
                                elif 'github.com' in link_url or 'gitlab.com' in link_url:
                                    link_type = 'repo'
                                else:
                                    link_type = 'source'
                                
                                links.append({
                                    'type': link_type,
                                    'text': link_text,
                                    'url': link_url
                                })
                        else:
                            # This is primarily a links line
                            for link_match in links_found:
                                link_text = link_match.group(1).strip()
                                link_url = link_match.group(2).strip()
                                
                                # Categorize link type based on URL
                                if link_url.startswith('./papers/') and link_url.endswith('.pdf'):
                                    link_type = 'internal_pdf'
                                elif 'github.com' in link_url or 'gitlab.com' in link_url:
                                    link_type = 'repo'
                                else:
                                    link_type = 'source'
                                
                                links.append({
                                    'type': link_type,
                                    'text': link_text,
                                    'url': link_url
                                })
                    else:
                        # Regular content line
                        summary_parts.append(line)
                
                # Join summary and clean up
                summary = ' '.join(summary_parts)
                # Remove link markdown from summary but keep the text
                summary = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', summary)
                
                # Determine entry type
                entry_type = 'paper'  # default
                if 'course' in title.lower() or 'tutorial' in summary.lower():
                    entry_type = 'course'
                elif ('framework' in title.lower() or 'tool' in title.lower() or 
                      any('github.com' in link['url'] for link in links)):
                    entry_type = 'tool'
                elif 'book' in summary.lower() or 'edited volume' in summary.lower():
                    entry_type = 'book'
                
                # Extract DOI or arXiv ID
                doi = None
                arxiv_id = None
                for link in links:
                    if 'arxiv.org' in link['url']:
                        arxiv_match = re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', link['url'])
                        if arxiv_match:
                            arxiv_id = arxiv_match.group(1)
                    elif 'doi.org' in link['url']:
                        doi_match = re.search(r'doi\.org/(.+)', link['url'])
                        if doi_match:
                            doi = doi_match.group(1)
                
                # Generate ID from first author's last name and year
                first_author = author.split(' et al.')[0] if ' et al.' in author else author
                # Handle complex author names
                if '&' in first_author:
                    first_author = first_author.split('&')[0].strip()
                if ',' in first_author:
                    # Format: "Last, First" or "Last, First & ..."
                    last_name = first_author.split(',')[0].strip()
                else:
                    # Format: "First Last" or "First Middle Last"
                    last_name = first_author.split()[-1] if first_author.split() else first_author
                
                last_name = last_name.lower().replace('.', '').replace(',', '')
                entry_id = f"{last_name}-{year}"
                
                entry = {
                    'id': entry_id,
                    'type': entry_type,
                    'title': title,
                    'author': author,
                    'year': year,
                    'section': current_section,
                    'subsection': current_subsection,
                    'summary': summary.strip(),
                    'links': links
                }
                
                if doi:
                    entry['doi'] = doi
                if arxiv_id:
                    entry['arxiv'] = arxiv_id
                
                entries.append(entry)
        else:
            i += 1
    
    return entries

def write_yaml_manually(entries, output_path):
    """Write YAML manually to avoid PyYAML dependency."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Agentic AI Bibliography\n')
        f.write('# Generated from README.md\n\n')
        
        for entry in entries:
            f.write('- id: ' + json.dumps(entry['id']) + '\n')
            f.write('  type: ' + json.dumps(entry['type']) + '\n')
            f.write('  title: ' + json.dumps(entry['title']) + '\n')
            f.write('  author: ' + json.dumps(entry['author']) + '\n')
            f.write('  year: ' + str(entry['year']) + '\n')
            if entry['section']:
                f.write('  section: ' + json.dumps(entry['section']) + '\n')
            if entry['subsection']:
                f.write('  subsection: ' + json.dumps(entry['subsection']) + '\n')
            
            # Write cross-references if they exist
            if 'cross_references' in entry and entry['cross_references']:
                f.write('  cross_references:\n')
                for cross_ref in entry['cross_references']:
                    f.write('    - section: ' + json.dumps(cross_ref['section']) + '\n')
                    if cross_ref.get('subsection'):
                        f.write('      subsection: ' + json.dumps(cross_ref['subsection']) + '\n')
                    f.write('      context: ' + json.dumps(cross_ref['context']) + '\n')
            
            f.write('  summary: >\n')
            # Write summary with proper indentation
            for line in entry['summary'].split('\n'):
                f.write('    ' + line.strip() + '\n')
            
            if 'doi' in entry:
                f.write('  doi: ' + json.dumps(entry['doi']) + '\n')
            if 'arxiv' in entry:
                f.write('  arxiv: ' + json.dumps(entry['arxiv']) + '\n')
            
            if entry['links']:
                f.write('  links:\n')
                for link in entry['links']:
                    f.write('    - type: ' + json.dumps(link['type']) + '\n')
                    f.write('      text: ' + json.dumps(link['text']) + '\n')
                    f.write('      url: ' + json.dumps(link['url']) + '\n')
            f.write('\n')

def main():
    """Main migration function."""
    if not README_PATH.exists():
        print(f"Error: {README_PATH} not found")
        return
    
    print(f"Reading from {README_PATH}")
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    print("Parsing bibliographic entries...")
    
    # Detect cross-references first
    print("Detecting cross-references...")
    cross_refs = detect_cross_references(readme_content)
    if cross_refs:
        print(f"Found cross-references for: {', '.join(cross_refs.keys())}")
    
    entries = parse_entries(readme_content)
    
    # Apply cross-references to entries
    if cross_refs:
        print("Applying cross-references to entries...")
        entries = apply_cross_references(entries, cross_refs)
    
    print(f"Found {len(entries)} entries")
    
    # Generate Table of Contents
    print("Generating Table of Contents...")
    toc_structure = generate_toc(readme_content)
    print(f"Found {len(toc_structure)} main sections")
    total_subsections = sum(len(section['subsections']) for section in toc_structure)
    print(f"Found {total_subsections} subsections")
    
    # Debug: Print first few entries with summaries
    if entries:
        print("\nFirst few entries with summaries:")
        for i, entry in enumerate(entries[:3]):
            print(f"  {i+1}. {entry['author']} - {entry['title']} ({entry['year']})")
            print(f"     Summary: {entry['summary'][:100]}..." if entry['summary'] else "     Summary: [EMPTY]")
    
    # Create output directory if it doesn't exist
    BIB_YML_PATH.parent.mkdir(exist_ok=True)
    
    print(f"Writing to {BIB_YML_PATH}")
    write_yaml_manually(entries, BIB_YML_PATH)
    
    print(f"Writing ToC to {TOC_YML_PATH}")
    write_toc_yaml(toc_structure, TOC_YML_PATH)
    
    print(f"Successfully migrated {len(entries)} entries to {BIB_YML_PATH}")
    print(f"Successfully generated ToC with {len(toc_structure)} sections to {TOC_YML_PATH}")

if __name__ == "__main__":
    main()
