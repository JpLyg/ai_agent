import sys

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent!")

    try:
        print("prompt:",sys.argv[1])
    except Exception as e:
        print("error:",e)
        SystemExit(1)
        sys.exit(1)
    else:
        ai_function(sys.argv[1])
    

def ai_function(string):

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=string
        )
    print(response.text)
    print("Prompt tokens:",response.usage_metadata.prompt_token_count)
    print("Response tokens:",response.usage_metadata.candidates_token_count)
    #return response


if __name__ == "__main__":
    main()
