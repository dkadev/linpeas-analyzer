# LinPEAS Analyzer

## Description

LinPEAS Analyzer is a versatile Python tool designed to streamline the process of privilege escalation analysis on Linux systems. It offers a user-friendly interface with a variety of commands to enhance your security assessments. Key features include:

- **Command Options:** LinPEAS Analyzer accepts multiple commands to perform different tasks, making it flexible for various use cases. Users can easily navigate through options to execute specific functions.

- **Usage Instructions:** The tool provides clear and concise instructions for each command, ensuring that users can quickly understand how to utilize its features effectively.

- **Banner Display:** Upon execution, LinPEAS Analyzer prints a visually appealing banner, enhancing the user experience and providing a professional touch.

- **LinPEAS Script Download:** Automatically download the latest version of the linPEAS bash script, ensuring you always have the most up-to-date tool for privilege escalation enumeration.

- **OpenAI API Key Configuration:** Easily configure your OpenAI API key within the tool to enable seamless integration with the GPT API for advanced analysis.

- **LinPEAS Output Analysis:** Pass the output of the linPEAS script to LinPEAS Analyzer, which will then utilize the GPT API to quickly identify potential privilege escalation paths, saving you time and effort in manual analysis.

With LinPEAS Analyzer, security professionals can enhance their Linux privilege escalation assessments with the power of automation and AI-driven insights.

## Usage Instructions

To use LinPEAS Analyzer, follow these steps:

1. Download the latest version of the tool from the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the tool using the command-line interface.

## Command Options

LinPEAS Analyzer supports the following command options:

- `--download`: Download the latest version of the linPEAS script.
- `--configure-api-key`: Configure your OpenAI API key.
- `--analyze-output`: Analyze the output of the linPEAS script using the GPT API.

## OpenAI API Key Configuration

To configure your OpenAI API key, use the following command:

```
python linpeas_analyzer.py --configure-api-key YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key.

## Example Usage

1. Download the latest linPEAS script:

```
python linpeas_analyzer.py --download
```

2. Configure your OpenAI API key:

```
python linpeas_analyzer.py --configure-api-key YOUR_API_KEY
```

3. Analyze the output of the linPEAS script:

```
python linpeas_analyzer.py --analyze-output /path/to/linpeas/output.txt
```

## Note

Ensure that you have a `config.txt` file in the same directory as `linpeas_analyzer.py` with the following content:

```
OPENAI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key.
