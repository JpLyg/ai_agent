from functions.get_files_info import *
from functions.run_python import *
#from functions.get_files_content import *
import config





print(run_python_file("calculator","main.py"))
print("******************")
print(run_python_file("calculator", "tests.py"))
print("******************")
print(run_python_file("calculator", "../main.py"))
print("******************")
print(run_python_file("calculator", "nonexistent.py"))
print("******************")