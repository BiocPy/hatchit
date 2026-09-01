from hatchit import create_hatchit_repository


def test_create_hatchit_repository_default(tmp_path):
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
    
    # Verify pyproject.toml name interpolation and pip structure
    with open(project_path / "pyproject.toml") as f:
        content = f.read()
        assert "my_test_project" in content
        assert "[project.optional-dependencies]" in content
        assert "[dependency-groups]" not in content

def test_create_hatchit_repository_with_uv(tmp_path):
    project_path = tmp_path / "my_uv_project"
    
    create_hatchit_repository(
        project_path=str(project_path),
        description="A test project",
        license="MIT",
        use_uv=True
    )
    
    # Verify pyproject.toml name interpolation and uv structure
    with open(project_path / "pyproject.toml") as f:
        content = f.read()
        assert "my_uv_project" in content
        assert "[dependency-groups]" in content
        assert "[project.optional-dependencies]" not in content
