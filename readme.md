\# Prompt Engineering Lab 2 - Baseline vs Enhanced Prompts



\## Description

This experiment compares a simple baseline prompt with an enhanced prompt

that includes role assignment, constraints, and output format instructions.



The program uses a local LLM through \*\*Ollama\*\*.



\## How to Run

1\. Make sure Ollama is installed and a model is pulled:

ollama pull llama3.2

2\. Install dependencies:

pip install -r requirements.txt

3\. Run the program:

python compare\_prompts.py

text## What the program does

\- Sends a baseline prompt: "What is recursion?"

\- Sends an enhanced prompt with role + analogy + length constraint

\- Prints both responses

\- Shows a short comparison analysis



\## Output

Screenshots of execution are available in the `output/` folder.



\## Notes

\- Uses Ollama (local LLM) instead of OpenAI to avoid API billing limits.

\- Same model and temperature are used for fair comparison.

