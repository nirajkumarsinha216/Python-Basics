from ollama_model import ask_llm

input_prompt = input("Enter your prompt: ")
response = ask_llm(input_prompt)

print("\nAI:")
print(response)   