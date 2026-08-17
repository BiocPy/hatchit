import pytest
import subprocess
from pathlib import Path

def test_cli_execution(tmp_path):
    project_path = tmp_path / "cli_project"
    
    # Run the CLI using the entrypoint if installed, or module
    result = subprocess.run(
        ["hatchit", str(project_path), "--description", "Test CLI package"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert "Hatching project" in result.stdout
    assert "Success!" in result.stdout
    
    # Verify core files were created by the CLI
    assert (project_path / "pyproject.toml").exists()
    assert (project_path / "CITATION.cff").exists()
    
    # Test error on non-empty directory
    (project_path / "extra.txt").touch()
    result_fail = subprocess.run(
        ["hatchit", str(project_path)],
        capture_output=True,
        text=True
    )
    
    assert result_fail.returncode == 1
    assert "is not empty" in result_fail.stdout
