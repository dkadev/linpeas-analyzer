import argparse
import requests
import os
import openai

def download_linpeas():
    url = "https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh"
    response = requests.get(url)
    with open("linpeas.sh", "wb") as file:
        file.write(response.content)
    print("Downloaded the latest linPEAS script.")

def configure_api_key(api_key):
    with open("config.txt", "w") as file:
        file.write(f"OPENAI_API_KEY={api_key}")
    print("Configured OpenAI API key.")

def get_openai_api_key():
    with open("config.txt", "r") as file:
        for line in file:
            if line.startswith("OPENAI_API_KEY="):
                return line.strip().split("=")[1]
    return None

def analyze_output(file_path):
    with open(file_path, "r") as file:
        output = file.read()
    
    api_key = get_openai_api_key()
    if not api_key:
        print("OpenAI API key not configured. Please configure it using --configure-api-key option.")
        return
    
    openai.api_key = api_key

    # Use Chat Completions API for a comprehensive analysis
    response = openai.ChatCompletion.create(
        model="o1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for analyzing linPEAS outputs."},
            {"role": "user", "content": f"Analyze the following linPEAS output for potential privilege escalation paths:\n\n{output}"}
        ],
        max_tokens=500,  # Adjust max_tokens as needed
        temperature=0.7  # Adjust temperature for response variability
    )

    print("GPT API Comprehensive Analysis Result:")
    print(response.choices[0].message['content'].strip())

def main():
    parser = argparse.ArgumentParser(description="LinPEAS Analyzer")
    parser.add_argument("--download", action="store_true", help="Download the latest version of the linPEAS script.")
    parser.add_argument("--configure-api-key", type=str, help="Configure your OpenAI API key.")
    parser.add_argument("--analyze-output", type=str, help="Analyze the output of the linPEAS script using the GPT API.")
    args = parser.parse_args()

    if args.download:
        download_linpeas()
    elif args.configure_api_key:
        configure_api_key(args.configure_api_key)
    elif args.analyze_output:
        analyze_output(args.analyze_output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
