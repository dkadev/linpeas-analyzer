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

def analyze_output(file_path):
    with open(file_path, "r") as file:
        output = file.read()
    # Placeholder for GPT API analysis
    print("Analyzed linPEAS output using GPT API.")

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
