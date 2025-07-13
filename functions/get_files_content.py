import os
import config 

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
        
        if len(file_content_string) == config.MAX_CHARS: file_content_string += f"[...File \"{file_path}\ truncated at 10000 characters]"

        return file_content_string
    
    except Exception as e:
        return f"Error: {e}"


#dir_target="lorem.txt"
#dir_base="calculator"

#print(get_file_content(dir_base, dir_target))