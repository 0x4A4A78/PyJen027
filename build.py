from pathlib import Path
import py_compile
import shutil

py_compile.compile("calculator.py", doraise=True)
Path("dist").mkdir(exist_ok=True)
shutil.copy2("calculator.py", "dist/calculator.py")
print("Build successful: dist/calculator.py")
