import argparse
import os
import sys

from .scaffold import create_hatchit_repository

__author__ = "Jayaram Kancherla"
__copyright__ = "Jayaram Kancherla"
__license__ = "MIT"


def main():
    parser = argparse.ArgumentParser(description="hatchit: Modern Python project scaffolder combining uv and hatch.")
    parser.add_argument("project_path", help="Path where the new project should be created.")
    parser.add_argument("--description", default="Add a short description here!", help="Optional project description.")
    parser.add_argument("--license", default="MIT", help="License to use. Defaults to MIT.")
    parser.add_argument("--use-uv", action="store_true", help="Use uv for dependency management and tox running.")

    args = parser.parse_args()

    project_path = args.project_path

    if os.path.exists(project_path) and os.listdir(project_path):
        print(f"Error: Directory {project_path} is not empty.")
        sys.exit(1)

    print(f"Hatching project at {project_path}...")
    create_hatchit_repository(project_path=project_path, description=args.description, license=args.license, use_uv=args.use_uv)
    print("Success! 🚀 💥")


if __name__ == "__main__":
    main()
