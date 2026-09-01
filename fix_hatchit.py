import sys
sys.path.append("/home/jayaram/.gemini/antigravity-ide/brain/9bc824b7-d246-454a-b7c0-32f2b65d7d0d/scratch")
import migrate_to_pip
from pathlib import Path

root = Path("/home/jayaram/Projects/biocpy/hatchit")
migrate_to_pip.process_tox_ini(root / "tox.ini")
migrate_to_pip.process_pyproject_toml(root / "pyproject.toml")
migrate_to_pip.process_github_action(root / ".github" / "workflows" / "run-tests.yml")
migrate_to_pip.process_github_action(root / ".github" / "workflows" / "publish-pypi.yml")
migrate_to_pip.process_readthedocs(root / ".readthedocs.yml")
