#!/usr/bin/env python3
"""
Main build script for Agentic AI Bibliography.
Runs consistency checks and exports to markdown.
"""

import sys
import subprocess
from pathlib import Path


def run_script(script_name: str, description: str) -> bool:
    """Run a Python script and return success status."""
    script_path = Path(__file__).parent / script_name

    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return False

    print(f"🔧 {description}...")

    try:
        # Use the same Python executable as the current process
        result = subprocess.run([
            sys.executable, str(script_path)
        ], capture_output=True, text=True, check=True)

        print(f"✅ {description} completed successfully")
        if result.stdout.strip():
            print(f"   Output: {result.stdout.strip()}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"   Exit code: {e.returncode}")
        if e.stdout.strip():
            print(f"   STDOUT: {e.stdout.strip()}")
        if e.stderr.strip():
            print(f"   STDERR: {e.stderr.strip()}")
        return False


def main():
    """Main build process."""
    print("🚀 Starting Agentic AI Bibliography Build Process")
    print("=" * 60)

    scripts_to_run = [
        ("check_consistency_simple.py", "Running consistency checks"),
        ("export_to_bibliography.py", "Exporting to bibliography markdown")
    ]

    all_success = True

    for script_name, description in scripts_to_run:
        success = run_script(script_name, description)
        if not success:
            all_success = False
            print(f"\n⚠️  Build process stopped due to error in {script_name}")
            break
        print()  # Add spacing between steps

    print("=" * 60)
    if all_success:
        print("🎉 Build process completed successfully!")
        print("📁 Generated files:")

        # List generated files
        bibliography_dir = Path(__file__).parent.parent / "bibliography"

        if bibliography_dir.exists():
            section_count = len([
                f for f in bibliography_dir.iterdir()
                if f.is_file() and f.suffix == '.md'
                and f.name != 'README.md'
            ])
            print(f"   Bibliography: {section_count} sections in "
                  f"{bibliography_dir}")
    else:
        print("❌ Build process failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
