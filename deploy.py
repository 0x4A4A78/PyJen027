"""Deploy the verified build to a local folder, then smoke test it."""
import os
from pathlib import Path
import shutil
import subprocess
import sys

target = Path(os.environ.get("DEPLOY_DIR", "deploy"))
target.mkdir(parents=True, exist_ok=True)
shutil.copy2("dist/calculator.py", target / "calculator.py")
run = subprocess.run([sys.executable, str(target / "calculator.py"), "12", "30"], capture_output=True, text=True, check=True)
assert "= 42" in run.stdout, run.stdout
print(f"Deployed to {target.resolve()}")
print(run.stdout)
