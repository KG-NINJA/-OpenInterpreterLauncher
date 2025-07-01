import subprocess 
import os 
interpreter_path = r"C:\\Program Files\\OpenAI\\Open Interpreter\\open-interpreter.exe" 
if os.path.exists(interpreter_path): 
   subprocess.run([interpreter_path]) 
else: 
   print("Open Interpreter is not installed or the path is incorrect.") 
