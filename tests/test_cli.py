import subprocess


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
    
    # Run the CLI with --use-uv
    project_path_uv = tmp_path / "cli_project_uv"
    result_uv = subprocess.run(
        ["hatchit", str(project_path_uv), "--description", "Test CLI package", "--use-uv"],
        capture_output=True,
        text=True
    )
    
    assert result_uv.returncode == 0
    assert "Hatching project" in result_uv.stdout
    assert (project_path_uv / "pyproject.toml").exists()
    with open(project_path_uv / "pyproject.toml") as f:
        assert "[dependency-groups]" in f.read()
    
    # Test error on non-empty directory
    (project_path / "extra.txt").touch()
    result_fail = subprocess.run(
        ["hatchit", str(project_path)],
        capture_output=True,
        text=True
    )
    
    assert result_fail.returncode == 1
    assert "is not empty" in result_fail.stdout
