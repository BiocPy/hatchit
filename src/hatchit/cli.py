import argparse
import os
import sys
from pathlib import Path
from hatchit.scaffold import create_hatchit_repository

def main():
    parser = argparse.ArgumentParser(
        description="hatchit: Modern Python project scaffolder combining uv and hatch."
    )
    parser.add_argument(
        "project_path",
        help="Path where the new project should be created."
    )
    parser.add_argument(
        "--description",
        default="Add a short description here!",
        help="Optional project description."
    )
    parser.add_argument(
        "--license",
        default="MIT",
        help="License to use. Defaults to MIT."
    )
    
    args = parser.parse_args()
    
    project_path = args.project_path
    
    if os.path.exists(project_path) and os.listdir(project_path):
        print(f"Error: Directory {project_path} is not empty.")
        sys.exit(1)
        
    print(f"Hatching project at {project_path}...")
    create_hatchit_repository(
        project_path=project_path,
        description=args.description,
        license=args.license
    )
    print("Success! 🚀 💥")

if __name__ == "__main__":
    main()
