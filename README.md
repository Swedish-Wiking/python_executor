# Python Executor

Enables drophandler on `.py` files as well as edit with VS Code on normal file open action.

## Installation

Build the executable using `pyinstaller` and place file at `C:\`. Execute the `.reg` file to add the drop-handler and open commands to `.py` files

### Build command

```cmd
pyinstaller --onefile --version-file=versioninfo.txt --icon=py.ico --noconsole python_executor.py
```
