import pytest
from pathlib import Path
from hatchit import create_hatchit_repository

def test_create_hatchit_repository(tmp_path):
    project_path = tmp_path / "my_test_project"
    
    create_hatchit_repository(
        project_path=str(project_path),
        description="A test project",
        license="MIT"
    )
    
    # Verify core files were created
    assert (project_path / "pyproject.toml").exists()
    assert (project_path / "README.md").exists()
    assert (project_path / "tox.ini").exists()
    assert (project_path / "CITATION.cff").exists()
    assert (project_path / ".zenodo.json").exists()
    assert (project_path / "docs" / "conf.py").exists()
    assert (project_path / ".github" / "workflows" / "run-tests.yml").exists()
    
    # Verify pyproject.toml name interpolation
    with open(project_path / "pyproject.toml") as f:
        content = f.read()
        assert "my-test-project" in content
