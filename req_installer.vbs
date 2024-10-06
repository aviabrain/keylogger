Set objShell = CreateObject("WScript.Shell")

' Path to the Python executable
pythonPath = "python"

' Command to install the pynput package
command = pythonPath & " -m pip install pynput"

' Run the command in a hidden window (0 = hidden, 1 = normal)
objShell.Run command, 0, True
