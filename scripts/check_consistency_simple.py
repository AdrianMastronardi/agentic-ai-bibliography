#!/usr/bin/env python3
"""
Consistency checker for Agentic AI Bibliography.
Cross-platform version without emojis for Windows compatibility.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Set, Dict, Any


def load_yaml_manually(file_path: Path) -> List[Dict]:
    """Manually parse YAML file to avoid dependency."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    current_entry: Dict[str, Any] = {}

    for line_num, line in enumerate(content.split('\n'), 1):
        stripped = line.strip()

        # Skip comments and empty lines
        if not stripped or stripped.startswith('#'):
            continue

        # Calculate indentation
        indent = len(line) - len(line.lstrip())

        # Handle list items
        if stripped.startswith('- '):
            if indent == 0:  # Top-level entry
                if current_entry:
                    entries.append(current_entry)
                current_entry = {}

            # Remove '- ' and process as key-value
            stripped = stripped[2:]

        # Handle key-value pairs
        if ':' in stripped:
            parts = stripped.split(':', 1)
            key = parts[0].strip().strip('"')
            value = parts[1].strip().strip('"') if len(parts) > 1 else ''

            if value:
                current_entry[key] = value

    # Add the last entry
    if current_entry:
        entries.append(current_entry)

    return entries


def parse_raw_toc_sections(file_path: Path) -> Set[str]:
    """Parse ToC sections from raw file content."""
    sections = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for section titles in ToC
        section_pattern = r'title:\s*["\']([^"\']+)["\']'
        matches = re.findall(section_pattern, content)

        for match in matches:
            # Clean up the title
            title = match.strip()
            if title and not title.lower().startswith('see also'):
                sections.add(title)

    except Exception as e:
        print(f"Warning: Could not parse ToC sections: {e}")

    return sections


def parse_raw_toc_subsections(file_path: Path) -> Set[str]:
    """Parse ToC subsections from raw file content."""
    subsections = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for subsection titles
        in_subsections = False
        for line in content.split('\n'):
            line = line.strip()

            if 'subsections:' in line:
                in_subsections = True
                continue

            if in_subsections:
                if line.startswith('- title:'):
                    # Extract subsection title
                    match = re.search(r'title:\s*["\']([^"\']+)["\']', line)
                    if match:
                        subsections.add(match.group(1).strip())
                elif (line and not line.startswith('-') and
                      not line.startswith(' ')):
                    # End of subsections block
                    in_subsections = False

    except Exception as e:
        print(f"Warning: Could not parse ToC subsections: {e}")

    return subsections


def check_consistency() -> Tuple[List[str], List[str]]:
    """Check consistency between bib.yml and toc.yml."""
    errors = []
    warnings: List[str] = []

    # File paths
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    bib_file = data_dir / "bib.yml"
    toc_file = data_dir / "toc.yml"

    # Check if files exist
    file_errors, files_valid = _validate_files_exist(data_dir)
    if not files_valid:
        return file_errors, warnings

    print("Parsing ToC file...")
    try:
        toc_sections = parse_raw_toc_sections(toc_file)
        toc_subsections = parse_raw_toc_subsections(toc_file)
        print(f"Found {len(toc_sections)} valid sections in ToC")
        print(f"Found {len(toc_subsections)} valid subsections in ToC")
    except Exception as e:
        errors.append(f"Error parsing ToC file: {e}")
        return errors, warnings

    print("Parsing bibliography file...")
    try:
        bib_entries = load_yaml_manually(bib_file)
        print(f"Found {len(bib_entries)} entries in bibliography")
    except Exception as e:
        errors.append(f"Error parsing bibliography file: {e}")
        return errors, warnings

    # Collect sections and subsections used in bibliography
    bib_sections, bib_subsections = _collect_bib_sections(bib_entries)

    print(f"\nSections used: {len(bib_sections)}/{len(toc_sections)}")
    print(f"Subsections used: {len(bib_subsections)}/{len(toc_subsections)}")

    # Check for missing sections
    missing_sections = bib_sections - toc_sections
    if missing_sections:
        for section in sorted(missing_sections):
            error_msg = f"Section '{section}' used in bibliography " \
                        f"but not found in ToC"
            errors.append(error_msg)

    # Check for missing subsections
    missing_subsections = bib_subsections - toc_subsections
    if missing_subsections:
        for subsection in sorted(missing_subsections):
            error_msg = f"Subsection '{subsection}' used in bibliography " \
                        f"but not found in ToC"
            errors.append(error_msg)

    # Check for unused sections (warning only)
    unused_sections = toc_sections - bib_sections
    if unused_sections:
        for section in sorted(unused_sections):
            warning_msg = f"Section '{section}' defined in ToC " \
                          f"but not used in bibliography"
            warnings.append(warning_msg)

    return errors, warnings


def _validate_files_exist(data_dir: Path) -> Tuple[List[str], bool]:
    """Validate that required files exist."""
    errors = []
    bib_file = data_dir / "bib.yml"
    toc_file = data_dir / "toc.yml"

    if not bib_file.exists():
        errors.append(f"Bibliography file not found: {bib_file}")
    if not toc_file.exists():
        errors.append(f"ToC file not found: {toc_file}")

    return errors, len(errors) == 0


def _collect_bib_sections(
        bib_entries: List[Dict]) -> Tuple[Set[str], Set[str]]:
    """Collect sections and subsections from bibliography entries."""
    bib_sections = set()
    bib_subsections = set()

    for entry in bib_entries:
        section = entry.get('section', '').strip()
        subsection = entry.get('subsection', '').strip()

        if section:
            bib_sections.add(section)
        if subsection:
            bib_subsections.add(subsection)

    return bib_sections, bib_subsections


def main():
    """Main consistency check function."""
    print("Running consistency check between bib.yml and toc.yml...")
    print("=" * 60)

    errors, warnings = check_consistency()

    # Report results
    if errors:
        print("\nERRORS FOUND:")
        for error in errors:
            print(f"   {error}")

    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"   {warning}")

    if not errors and not warnings:
        print("\nAll consistency checks passed!")
        print("   - All sections in bib.yml exist in toc.yml")
        print("   - All subsections in bib.yml exist in toc.yml")

    print("\n" + "=" * 60)

    # Exit with appropriate code
    if errors:
        print("Consistency check failed")
        sys.exit(1)
    else:
        print("Consistency check completed successfully")
        sys.exit(0)


if __name__ == "__main__":
    main()
