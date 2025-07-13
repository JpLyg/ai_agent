from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "working_directory":types.Schema(
                type=types.Type.STRING,
                description="The working directory of the file.",
            )
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return the content of the file if its a valid file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The content of the file to be opened.",
            ),
            "working_directory":types.Schema(
                type=types.Type.STRING,
                description="The working directory of the file.",
            )
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified Python program.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The returned value of the python prgogram.",
            ),
            "working_directory":types.Schema(
                type=types.Type.STRING,
                description="The working directory of the file.",
            )
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or update a file in the provided directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file and its size.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content written in the created file",
            ),
            "working_directory":types.Schema(
                type=types.Type.STRING,
                description="The working directory of the file.",
            )
    
        },
    ),
)