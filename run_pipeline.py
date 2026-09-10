"""
Master execution script for the Bluestock Mutual Fund Analytics project.

This script provides a single entry point for running the project's
data ingestion and analytics workflow.
"""

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def run_script(script_name):
    """Run a Python script from the project root."""
    script_path = PROJECT_ROOT / script_name

    if not script_path.exists():
        print(f"Skipping {script_name}: file not found.")
        return False

    print(f"Running {script_name}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=False
    )

    if result.returncode != 0:
        print(f"{script_name} finished with errors.")
        return False

    print(f"{script_name} completed successfully.")
    return True


def main():
    """Run the project pipeline."""
    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    scripts = [
        "data_ingestion.py",
        "data_quality.py",
    ]

    results = [run_script(script) for script in scripts]

    print("=" * 60)

    if all(results):
        print("Pipeline completed successfully.")
    else:
        print("Pipeline completed with one or more skipped/failed steps.")

    print("=" * 60)


if __name__ == "__main__":
    main()