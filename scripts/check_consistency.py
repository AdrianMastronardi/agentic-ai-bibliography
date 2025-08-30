#!/usr/bin/env python3
"""
Consistency check script for Agentic AI Bibliography.
Verifies that section and subsection references in bib.yml exist in toc.yml.
"""
import json
import sys
from pathlib import Path

BIB_YML_PATH = Path(__file__).parent.parent / "data" / "bib.yml"
TOC_YML_PATH = Path(__file__).parent.parent / "data" / "toc.yml"

def parse_yaml_manually(file_path):
    """Parse YAML manually to avoid external dependencies."""
    data = []
    current_entry = None
    in_summary = False
    current_list_key = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        original_line = line
        line = line.rstrip()
        
        # Skip comments and empty lines
        if line.strip().startswith('#') or not line.strip():
            continue
            
        # Handle summary blocks (multiline with >)
        if in_summary:
            if line and (line.startswith('  ') or line.strip() == ''):
                # Continue summary content (ignore for our purposes)
                continue
            else:
                # End of summary block
                in_summary = False
        
        # Handle top-level key followed by list (like toc:)
        if ':' in line and not line.startswith(' ') and not line.startswith('-'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if not value:  # Key followed by list on next lines
                current_list_key = key
                current_entry = {key: []}
                continue
        
        # Start of new entry
        if line.startswith('- '):
            # If we're in a list context, add to current list
            if current_list_key and current_entry:
                new_item = {}
                # Parse the first field in the entry line
                if ':' in line:
                    key, value = line[2:].split(':', 1)
                    new_item[key.strip()] = json.loads(value.strip())
                current_entry[current_list_key].append(new_item)
                current_item = new_item
            else:
                # Regular entry parsing
                if current_entry:
                    data.append(current_entry)
                current_entry = {}
                current_list_key = None
                # Parse the first field in the entry line
                if ':' in line:
                    key, value = line[2:].split(':', 1)
                    current_entry[key.strip()] = json.loads(value.strip())
        elif current_entry and ':' in line and not line.startswith('    '):
            # Top-level field in current entry (not nested under links, etc.)
            if line.startswith('  ') and not line.startswith('    '):
                key, value = line.strip().split(':', 1)
                value = value.strip()
                
                if value == '>':
                    in_summary = True
                    continue
                elif not value:  # Key with nested content
                    # Handle nested structures like subsections:
                    if current_list_key and len(current_entry[current_list_key]) > 0:
                        current_entry[current_list_key][-1][key.strip()] = []
                elif value and not value.startswith('-'):
                    try:
                        if current_list_key and len(current_entry[current_list_key]) > 0:
                            current_entry[current_list_key][-1][key.strip()] = json.loads(value)
                        else:
                            current_entry[key.strip()] = json.loads(value)
                    except:
                        if current_list_key and len(current_entry[current_list_key]) > 0:
                            current_entry[current_list_key][-1][key.strip()] = value.strip('"')
                        else:
                            current_entry[key.strip()] = value.strip('"')
        elif line.startswith('      - '):
            # Handle nested list items (like subsections)
            if current_list_key and len(current_entry[current_list_key]) > 0:
                last_item = current_entry[current_list_key][-1]
                # Find the key that should contain this list
                for key in last_item:
                    if isinstance(last_item[key], list):
                        nested_item = {}
                        if ':' in line:
                            subkey, subvalue = line[8:].split(':', 1)  # Remove '      - '
                            nested_item[subkey.strip()] = json.loads(subvalue.strip())
                        last_item[key].append(nested_item)
                        break
        
    if current_entry:
        data.append(current_entry)
    
    return data

def extract_sections_from_toc(toc_data):
    """Extract valid sections and subsections from ToC data."""
    valid_sections = set()
    valid_subsections = set()
    
    # Find the toc section
    toc_entries = None
    for item in toc_data:
        if isinstance(item, dict) and 'toc' in item:
            toc_entries = item['toc']
            break
    
    if not toc_entries or len(toc_entries) == 0:
        # Try alternative parsing - look for entries under 'toc:'
        with open(TOC_YML_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple regex-based parsing for toc entries
        import re
        
        # Find main sections (those that start with numbers like "1.", "2.", etc. at beginning of line after "- title:")
        section_pattern = r'- title: "(\d+\. [^"]+)"'
        section_matches = re.findall(section_pattern, content)
        for match in section_matches:
            valid_sections.add(match)
        
        # Find subsections (those with format like "2.1", "2.2" etc. with indentation)
        subsection_pattern = r'  - title: "(\d+\.\d+ [^"]+)"'
        subsection_matches = re.findall(subsection_pattern, content)
        for match in subsection_matches:
            valid_subsections.add(match)
    else:
        # Parse structured toc data
        for section in toc_entries:
            if isinstance(section, dict) and 'title' in section:
                valid_sections.add(section['title'])
                
                if 'subsections' in section:
                    for subsection in section['subsections']:
                        if isinstance(subsection, dict) and 'title' in subsection:
                            valid_subsections.add(subsection['title'])
    
    return valid_sections, valid_subsections

def check_consistency():
    """Check consistency between bib.yml and toc.yml."""
    errors = []
    warnings = []
    
    # Check if files exist
    if not BIB_YML_PATH.exists():
        errors.append(f"Bibliography file not found: {BIB_YML_PATH}")
        return errors, warnings
    
    if not TOC_YML_PATH.exists():
        errors.append(f"ToC file not found: {TOC_YML_PATH}")
        return errors, warnings
    
    try:
        # Parse ToC file
        print("Parsing ToC file...")
        toc_data = parse_yaml_manually(TOC_YML_PATH)
        valid_sections, valid_subsections = extract_sections_from_toc(toc_data)
        
        print(f"Found {len(valid_sections)} valid sections in ToC")
        print(f"Found {len(valid_subsections)} valid subsections in ToC")
        
        # Parse bibliography file
        print("Parsing bibliography file...")
        bib_data = parse_yaml_manually(BIB_YML_PATH)
        
        print(f"Found {len(bib_data)} entries in bibliography")
        
        # Check each entry
        entries_with_issues = []
        sections_used = set()
        subsections_used = set()
        
        for entry in bib_data:
            entry_id = entry.get('id', 'unknown')
            entry_issues = []
            
            # Check section
            section = entry.get('section')
            if section:
                sections_used.add(section)
                if section not in valid_sections:
                    entry_issues.append(f"Invalid section: '{section}'")
            else:
                entry_issues.append("Missing section field")
            
            # Check subsection (optional)
            subsection = entry.get('subsection')
            if subsection:
                subsections_used.add(subsection)
                if subsection not in valid_subsections:
                    entry_issues.append(f"Invalid subsection: '{subsection}'")
            
            # Check cross-references and mark their sections/subsections as used
            cross_refs = entry.get('cross_references', [])
            for cross_ref in cross_refs:
                cross_section = cross_ref.get('section')
                cross_subsection = cross_ref.get('subsection')
                
                if cross_section:
                    sections_used.add(cross_section)
                if cross_subsection:
                    subsections_used.add(cross_subsection)
            
            if entry_issues:
                entries_with_issues.append({
                    'id': entry_id,
                    'issues': entry_issues
                })
        
        # Report errors
        if entries_with_issues:
            errors.append(f"Found {len(entries_with_issues)} entries with section/subsection issues:")
            for entry in entries_with_issues:
                errors.append(f"  - {entry['id']}: {', '.join(entry['issues'])}")
        
        # Report unused sections/subsections
        # Also check for cross-references in the raw file content
        with open(BIB_YML_PATH, 'r', encoding='utf-8') as f:
            bib_content = f.read()
        
        # Look for cross-references in the raw content to catch any the parser missed
        for section_title in valid_sections:
            if f'section: "{section_title}"' in bib_content:
                sections_used.add(section_title)
        
        for subsection_title in valid_subsections:
            if f'subsection: "{subsection_title}"' in bib_content:
                subsections_used.add(subsection_title)
        
        unused_sections = valid_sections - sections_used
        if unused_sections:
            warnings.append(f"Unused sections in ToC: {', '.join(sorted(unused_sections))}")
        
        unused_subsections = valid_subsections - subsections_used
        if unused_subsections:
            warnings.append(f"Unused subsections in ToC: {', '.join(sorted(unused_subsections))}")
        
        # Summary
        print(f"\nSections used: {len(sections_used)}/{len(valid_sections)}")
        print(f"Subsections used: {len(subsections_used)}/{len(valid_subsections)}")
        
    except Exception as e:
        errors.append(f"Error during consistency check: {str(e)}")
    
    return errors, warnings

def main():
    """Main consistency check function."""
    print("🔍 Running consistency check between bib.yml and toc.yml...")
    print("=" * 60)
    
    errors, warnings = check_consistency()
    
    # Report results
    if errors:
        print("\n❌ ERRORS FOUND:")
        for error in errors:
            print(f"   {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   {warning}")
    
    if not errors and not warnings:
        print("\n✅ All consistency checks passed!")
        print("   - All sections in bib.yml exist in toc.yml")
        print("   - All subsections in bib.yml exist in toc.yml")
    
    print("\n" + "=" * 60)
    
    # Exit with appropriate code
    if errors:
        print("❌ Consistency check failed")
        sys.exit(1)
    else:
        print("✅ Consistency check completed successfully")
        sys.exit(0)

if __name__ == "__main__":
    main()
