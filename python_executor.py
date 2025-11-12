import sys
import subprocess
from shutil import which

args = sys.argv[1:]  # Skip the script filename

vs_code = which("code")
python_exe = which("python")
CREATE_NO_WINDOW = 0x08000000

if len(args) == 0:
    if python_exe:
        cmd = [
            "cmd.exe",
            "/k",
            "TITLE",
            "Python",
            "&",
            python_exe,
            "&",
            "pause",
            "&",
            "exit",
        ]
        subprocess.run(cmd)
elif len(args) == 1:
    if vs_code:
        subprocess.run([vs_code, args[0]], creationflags=CREATE_NO_WINDOW)
else:
    if python_exe:
        cmd = [
            "cmd.exe",
            "/k",
            "TITLE",
            "Python",
            "&",
            python_exe,
            *args,
            "&",
            "pause",
            "&",
            "exit",
        ]
        subprocess.run(cmd, creationflags=0)
