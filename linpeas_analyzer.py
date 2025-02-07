import argparse
import requests
import os
import openai
from openai import OpenAI
import dotenv
import yaml
from rich.console import Console
from rich.markdown import Markdown

dotenv.load_dotenv()

def print_banner():
    banner = """
#  ▗▖   ▗▄▄▄▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖ ▗▄▖  ▗▄▄▖     ▗▄▖ ▗▖  ▗▖ ▗▄▖ ▗▖ ▗▖  ▗▖▗▄▄▄▄▖▗▄▄▄▖▗▄▄▖ 
#  ▐▌     █  ▐▛▚▖▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌       ▐▌ ▐▌▐▛▚▖▐▌▐▌ ▐▌▐▌  ▝▚▞▘    ▗▞▘▐▌   ▐▌ ▐▌
#  ▐▌     █  ▐▌ ▝▜▌▐▛▀▘ ▐▛▀▀▘▐▛▀▜▌ ▝▀▚▖    ▐▛▀▜▌▐▌ ▝▜▌▐▛▀▜▌▐▌   ▐▌   ▗▞▘  ▐▛▀▀▘▐▛▀▚▖
#  ▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▌   ▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘    ▐▌ ▐▌▐▌  ▐▌▐▌ ▐▌▐▙▄▄▖▐▌  ▐▙▄▄▄▖▐▙▄▄▖▐▌ ▐▌
#                                                                                   
    """
    print(banner)

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

def analyze_output(file_path, model, max_tokens, temperature, user):
    with open(file_path, "r") as file:
        output = file.read()
    
    api_key = get_openai_api_key()
    if not api_key:
        print("OpenAI API key not configured. Please configure it using --configure-api-key option.")
        return
    
    openai.api_key = api_key

    client = OpenAI()

    print("Analyzing linPEAS output using GPT API...")

    # Use Chat Completions API for a comprehensive analysis
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for analyzing linPEAS outputs. Focus on providing quick ways of privilege escalation or lateral movement. Ensure the output is in an ordered markdown format. Include command examples to try. Add a top-ranking summary of next moves at the end."},
            {"role": "user", "content": f"Analyze the following linPEAS output for potential privilege escalation paths. The user running linpeas is: {user}.\n\n{output}"}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )

    print("GPT API Comprehensive Analysis Result:")
    formatted_message = format_message(completion.choices[0].message.content)

    console = Console()

    md = Markdown(formatted_message)
    console.print(md)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="LinPEAS Analyzer")
    parser.add_argument("-d", "--download", action="store_true", help="Download the latest version of the linPEAS script.")
    parser.add_argument("-a", "--analyze-output", type=str, help="Analyze the output of the linPEAS script using the GPT API.")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="Specify the model to use for analysis.")
    parser.add_argument("--max-tokens", type=int, default=500, help="Specify the maximum number of tokens for the response.")
    parser.add_argument("--temperature", type=float, default=0.7, help="Specify the temperature for response variability.")
    parser.add_argument("--config-file", type=str, help="Specify a YAML configuration file for settings.")
    parser.add_argument("--user", type=str, help="Specify the user that is running linpeas.")
    args = parser.parse_args()

    if args.config_file:
        with open(args.config_file, "r") as file:
            config = yaml.safe_load(file)
            model = config.get("model", "gpt-4o-mini")
            max_tokens = config.get("max_tokens", 500)
            temperature = config.get("temperature", 0.7)
            user = config.get("user", "unknown")
    else:
        model = args.model
        max_tokens = args.max_tokens
        temperature = args.temperature
        user = args.user if args.user else "unknown"

    if args.download:
        download_linpeas()
    elif args.analyze_output:
        analyze_output(args.analyze_output, model, max_tokens, temperature, user)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
