from openai import OpenAI

def send_prompt(client, prompt, model="llama3.2"):
    """Send a prompt to the local Ollama model and return the response."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


def main():
    try:
        print("✅ Connecting to Ollama...\n")

        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

        # ---------- BASELINE PROMPT ----------
        baseline_prompt = "What is recursion?"

        print("=" * 50)
        print("=== BASELINE PROMPT ===")
        print("=" * 50)
        print(f"Prompt: {baseline_prompt}\n")

        baseline_response = send_prompt(client, baseline_prompt)
        print("Response:")
        print(baseline_response)

        # ---------- ENHANCED PROMPT ----------
        enhanced_prompt = (
            "You are a computer science professor. "
            "Explain recursion to a beginner using a real-world analogy. "
            "Keep your explanation to exactly 3 sentences."
        )

        print("\n" + "=" * 50)
        print("=== ENHANCED PROMPT ===")
        print("=" * 50)
        print(f"Prompt: {enhanced_prompt}\n")

        enhanced_response = send_prompt(client, enhanced_prompt)
        print("Response:")
        print(enhanced_response)

        # ---------- SIMPLE ANALYSIS ----------
        print("\n" + "=" * 50)
        print("=== COMPARISON ANALYSIS ===")
        print("=" * 50)
        print(f"Baseline length : {len(baseline_response.split())} words")
        print(f"Enhanced length : {len(enhanced_response.split())} words")
        print("\nObservation:")
        print("- Baseline gives a general technical definition.")
        print("- Enhanced prompt adds role, analogy, and length control,")
        print("  making the answer clearer and more beginner-friendly.")

        print("\n✅ Experiment 2 completed successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure Ollama is running and the model is available.")
        print("Try: ollama list")


if __name__ == "__main__":
    main()