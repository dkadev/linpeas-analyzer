# LinPEAS Analyzer

## Description

LinPEAS Analyzer is a versatile Python tool designed to streamline the process of privilege escalation analysis on Linux systems. It offers a user-friendly interface with a variety of commands to enhance your security assessments. Key features include:

- **LinPEAS Script Download:** Automatically download the latest version of the linPEAS bash script, ensuring you always have the most up-to-date tool for privilege escalation enumeration.

- **LinPEAS Output Analysis:** Pass the output of the linPEAS script to LinPEAS Analyzer, which will then utilize the GPT API to quickly identify potential privilege escalation paths, saving you time and effort in manual analysis.

With LinPEAS Analyzer, security professionals can enhance their Linux privilege escalation assessments with the power of automation and AI-driven insights.

## Usage Instructions

To use LinPEAS Analyzer, follow these steps:

1. Download the latest version of the tool from the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the tool using the command-line interface.

## Command Options

LinPEAS Analyzer supports the following command options:

- `-d`, `--download`: Download the latest version of the linPEAS script.
- `-a`, `--analyze-output`: Analyze the output of the linPEAS script using the GPT API.
- `--model`: Specify the model to use for analysis.
- `--max-tokens`: Specify the maximum number of tokens for the response.
- `--temperature`: Specify the temperature for response variability.
- `--config-file`: Specify a YAML configuration file for settings.
- `--user`: Specify the user that is running linpeas.

## OpenAI API Key Configuration

To configure your OpenAI API key, create a `.env` file in the same directory as `linpeas_analyzer.py` with the following content:

```shell
OPENAI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key.

## Example Usage

Download the latest linPEAS script:

```shell
python linpeas_analyzer.py -d
```

Analyze the output of the linPEAS script:

```shell
python linpeas_analyzer.py -a /path/to/linpeas/output.txt
```

Analyze the output of the linPEAS script with optional arguments:

```shell
python linpeas_analyzer.py -a /path/to/linpeas/output.txt --model gpt-4 --max-tokens 1000 --temperature 0.5
```

Analyze the output of the linPEAS script using a configuration file:

```shell
python linpeas_analyzer.py -a /path/to/linpeas/output.txt --config-file config.yaml
```

Analyze the output of the linPEAS script specifying the user:

```shell
python linpeas_analyzer.py -a /path/to/linpeas/output.txt --user username
```
