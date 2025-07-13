import sys
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
from google import genai
client = genai.Client(api_key=api_key)
from google.genai import types
from schema_info import *
from functions.get_files_info import *


def main():
    verbose = False
    if '-v' in sys.argv or '--verbose' in sys.argv: verbose= True    #>> This line is the conditional statement for checking if its verbose or not.
        
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model_name = "gemini-2.0-flash-001"

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
      ]
    )

    print("Hello from ai-agent!")

    try:
        inquiry = sys.argv[1]
    except Exception as e:
        print("error:",e)
        SystemExit(1)
        sys.exit(1)
    else:

        messages = [
             types.Content(role="user", parts=[types.Part(text=inquiry)]),
            ]
        
        response=ai_function(sys.argv[1],messages,model_name,system_prompt,available_functions,verbose)


            #ai_follow_up(response,inquiry)
    
def ai_function(string,messages,model_name,system_prompt,available_functions,verbose):

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],
            system_instruction=system_prompt
            )
)
    if response.function_calls: 
        procesed_call = call_function (response.function_calls[0],verbose)

        print(f"-> {procesed_call.parts[0].function_response.response}")

    else: print(response.text)

    #call_function(response.function_calls[0],True)
    #return response

def ai_follow_up(response,inquiry):
    print("User prompt:",inquiry)
    print("Prompt tokens:",response.usage_metadata.prompt_token_count)
    print("Response tokens:",response.usage_metadata.candidates_token_count)


def call_function(function_call_part, verbose=False):
    func_to_use = function_call_part.args.copy()
    func_to_use["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {function_call_part.name}({func_to_use})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    target_function = function_list.get(function_call_part.name)

    if not target_function:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                 ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": target_function(**func_to_use)},
            )
        ],
    )

    
 















if __name__ == "__main__":
    main()
