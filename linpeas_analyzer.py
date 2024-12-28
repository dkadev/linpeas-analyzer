import argparse
import requests
import os
import openai
import dotenv

dotenv.load_dotenv()

def download_linpeas():
    url = "https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh"
    response = requests.get(url)
    with open("linpeas.sh", "wb") as file:
        file.write(response.content)
    print("Downloaded the latest linPEAS script.")

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

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
