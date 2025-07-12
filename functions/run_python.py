import os
import subprocess
#import config 

def run_python_file(working_directory, file_path):
    try:


        target_file = os.path.abspath(os.path.join(working_directory,file_path))
        file_dir = os.path.dirname(target_file)

        print()
        print("target_folder:",target_file)
        #print("file type:", file_path[-3:])

        if not target_file.startswith(os.path.abspath(working_directory)):
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.exists(target_file):
            return f'Error: File "{file_path}" not found.'
        
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'


        
        result = subprocess.run(
            ["python",file_path],
            timeout=30,
            capture_output=True,
            text=True,
            cwd=working_directory)
        
        rtr_str = []

        if result.stdout: 
            rtr_str.append(f"STDOUT: {result.stdout}")
    
        else:
            rtr_str.append("No output produced.") 

        if result.stderr: 
            rtr_str.append(f"STDERR: {result.stderr}")

        if result.returncode != 0:
            rtr_str.append(f"Process exited with code {result.returncode}")

        return ("\n").join(rtr_str)
        
        
    except Exception as e:
        return f"Error: executing Python file: {e}"


