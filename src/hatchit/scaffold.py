import subprocess
from pathlib import Path
from warnings import warn
import copier

__author__ = "Jayaram Kancherla"
__copyright__ = "Jayaram Kancherla"
__license__ = "MIT"


def create_hatchit_repository(project_path: str, description: str, license: str) -> None:
    """Create a new Python project using uv and hatch.

    This function initializes a new Python project at the specified `project_path`
    using the `uv` tool and `hatch` for version management and project scaffolding.
    It uses `copier` under the hood to render the project template.

    Args:
        project_path:
            The path where the new project should be created.

        description:
            A short description of the project.

        license:
            The license to use for the project.

    Example:
        >>> create_hatchit_repository(
        ...     "my_project",
        ...     description="My new project",
        ...     license="MIT",
        ... )
    """
    if description is None:
        description = "Add a short description here!"

    try:
        git_name = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
        git_email = subprocess.check_output(["git", "config", "user.email"], text=True).strip()
    except Exception:
        warn("Git user.name and user.email not configured. Using default values.")
        git_name = "First Author"
        git_email = "first.author@example.com"
        
    try:
        # Check if gh CLI is installed for github username, or extract from remote if any.
        # Defaults to a placeholder
        github_username = "YOUR_ORG_OR_USERNAME"
    except Exception:
        github_username = "YOUR_ORG_OR_USERNAME"

    proj_name = Path(project_path).parts[-1]

    data = {
        "project_name": proj_name,
        "description": description,
        "license": license,
        "author_name": git_name,
        "author_email": git_email,
        "github_username": github_username,
    }

    template_dir = Path(__file__).parent.parent.parent
    if not (template_dir / "copier.yml").exists():
        # Fallback for when the package is installed
        template_dir = Path(__file__).parent

    copier.run_copy(str(template_dir), project_path, data=data, unsafe=True)
    
    print("hatchit complete! 🚀 💥")
