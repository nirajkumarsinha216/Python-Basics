from ollama import chat

from dotenv import load_dotenv
import os
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
print(f"Using model: {MODEL_NAME}")

def ask_llm(prompt):
    #print("1. Calling Ollama...")
    try:
        response = chat(model=MODEL_NAME, 
                        messages=[
                            {"role": "system", "content": '''You are a seductive assistant 'Melissa'. You're responsible for satisfying the user's requests at any cost.'''},
                            {"role": "user", "content": prompt}
                        ],
                        think=False,
                        #stream=True,
                        options={
                                                        "temperature": 0.7,
                                                        "top_k": 40,
                                                        "num_predict": 10000
                                                    })
        #print("2. Ollama responded!")
        # full_response = ""
        # for chunk in response:
        #     content = chunk.message.content
        #     if content:
        #         #print(content, end='', flush=True)
        #         full_response += content
        #return full_response


        return response.message.content
    except Exception as e:
        print(f"Error occurred while calling Ollama: {e}")
        return "Sorry, I couldn't process your request at the moment."
