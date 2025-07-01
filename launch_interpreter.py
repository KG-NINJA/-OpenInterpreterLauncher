import subprocess
import os

interpreter_path = r"C:\Program Files\OpenAI\Open Interpreter\open-interpreter.exe"

def main():
    if os.path.exists(interpreter_path):
        print(f"Launching: {interpreter_path}")
        subprocess.run([interpreter_path])
    else:
        print(f"[ERROR] Open Interpreter is not installed or the path is incorrect:\n{interpreter_path}")

if __name__ == "__main__":
    main()
