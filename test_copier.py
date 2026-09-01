import copier
import tempfile
import os

with tempfile.TemporaryDirectory() as temp_dir:
    copier.run_copy(".", temp_dir, data={"project_name": "test", "description": "test", "license": "MIT", "use_uv": False}, vcs_ref="HEAD", unsafe=True, defaults=True)
    print("Success")
