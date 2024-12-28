import argparse
import requests
import os
import openai
from openai import OpenAI
import dotenv
from rich.console import Console
from rich.markdown import Markdown

dotenv.load_dotenv()

def download_linpeas():
    url = "https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh"
    response = requests.get(url)
    with open("linpeas.sh", "wb") as file:
        file.write(response.content)
    print("Downloaded the latest linPEAS script.")

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def format_message(message):
    formatted_message = "\n".join(line.strip() for line in message.split("\n") if line.strip())
    return formatted_message

def analyze_output(file_path):
    with open(file_path, "r") as file:
        output = file.read()
    
    api_key = get_openai_api_key()
    if not api_key:
        print("OpenAI API key not configured. Please configure it using --configure-api-key option.")
        return
    
    openai.api_key = api_key

    client = OpenAI()

    # Use Chat Completions API for a comprehensive analysis
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for analyzing linPEAS outputs."},
            {"role": "user", "content": f"Analyze the following linPEAS output for potential privilege escalation paths:\n\n{output}"}
        ],
        max_tokens=500,  # Adjust max_tokens as needed
        temperature=0.7  # Adjust temperature for response variability
    )

    print("GPT API Comprehensive Analysis Result:")
    formatted_message = format_message(completion.choices[0].message.content)

    console = Console()

    md = Markdown(formatted_message)
    console.print(md)

def main():
    parser = argparse.ArgumentParser(description="LinPEAS Analyzer")
    parser.add_argument("-d", "--download", action="store_true", help="Download the latest version of the linPEAS script.")
    parser.add_argument("-a", "--analyze-output", type=str, help="Analyze the output of the linPEAS script using the GPT API.")
    args = parser.parse_args()

    if args.download:
        download_linpeas()
    elif args.analyze_output:
        analyze_output(args.analyze_output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
