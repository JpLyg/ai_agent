import os
#import config 
#from functions.get_files_info import get_files_info

def get_files_info(working_directory, directory=None):
    
    if directory is None or directory == ".": 
        directory = "."
        directory_name = "current"
    else: directory_name = "'"+directory+"'"
    try:
        target_dir = os.path.join(working_directory, directory)
        target_dir = os.path.abspath(target_dir)

        print()
        print("target_Dir:",target_dir)

        print(f"Result for {directory_name} directory:")
        
        if not target_dir.startswith(os.path.abspath(working_directory)):
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        
        if not os.path.isdir(target_dir): 
            return f'Error: "{directory}" is not a directory'
        
        #dir_content_checker(target_dir)
        for item in os.listdir(target_dir):
            current_dir = os.path.join(target_dir, item)
            file_size = os.path.getsize(current_dir)
            is_dir = os.path.isdir(current_dir)

            print(
                f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            )
    except Exception as e:
        return f"Error: {e}"
    
    return ""
   
def get_file_content(working_directory, file_path):

    try:
        target_file = os.path.abspath(os.path.join(working_directory,file_path))

        print()
        print("target_Dir:",target_file)

        if not target_file.startswith(os.path.abspath(working_directory)):
                return f"Error: Cannot list \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.isfile(target_file): 
                return f"Error: File not found or is not a regular file: \"{file_path}\""
        
        with open(target_file, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            #print("test file:",file_content_string)
        
        if len(file_content_string) == config.MAX_CHARS: file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"

        return file_content_string
    
    except Exception as e:
        return f"Error: {e}"

def write_file(working_directory, file_path, content=None): 
    try:


        target_file = os.path.abspath(os.path.join(working_directory,file_path))
        file_dir = os.path.dirname(target_file)

        print()
        print("target_folder:",file_dir)
        

        if not target_file.startswith(os.path.abspath(working_directory)):
            return f"Error: Cannot list \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(target_file, "w") as f:
             f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"

