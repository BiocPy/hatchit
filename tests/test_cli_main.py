import sys
import pytest
from unittest.mock import patch, MagicMock
from hatchit.cli import main
import os

def test_cli_main_success(tmp_path, capsys):
    project_path = tmp_path / "cli_main_project"
    
    with patch.object(sys, "argv", ["hatchit", str(project_path), "--description", "Desc", "--use-uv"]):
        main()
        
    captured = capsys.readouterr()
    assert "Hatching project" in captured.out
    assert "Success!" in captured.out
    assert (project_path / "pyproject.toml").exists()

def test_cli_main_directory_not_empty(tmp_path, capsys):
    project_path = tmp_path / "cli_main_project_fail"
    project_path.mkdir()
    (project_path / "file.txt").touch()
    
    with patch.object(sys, "argv", ["hatchit", str(project_path)]):
        with pytest.raises(SystemExit) as excinfo:
            main()
    
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "is not empty" in captured.out
