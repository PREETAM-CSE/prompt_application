import streamlit as st
from openai import OpenAI
import os
import time

def gpt_chat(prompt):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    messages = list()
    system_prompt = "Answer as concisely as possible"
    messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )
    current_response = response.choices[0].message.content
    return current_response

def interactive_chat():
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    questions = list()
    bot_responses = list()
    messages = list()
    
    # Get system prompt from user
    print("Enter system prompt (or press Enter for default):")
    try:
        system_prompt = input("System: ").strip()
        if not system_prompt:
            system_prompt = "Answer as concisely as possible"
        print(f"Using system prompt: '{system_prompt}'")
    except EOFError:
        system_prompt = "Answer as concisely as possible"
        print(f"Using default system prompt: '{system_prompt}'")
    
    messages.append({"role": "system", "content": system_prompt})
    print("-" * 50)
    
    try:
        while True:
            current_question = input("Me: ")
            if current_question.lower() in ["exit", "quit", "bye"]:
                print("Bot: Bye!")
                time.sleep(2)
                break
            if current_question.lower() in ["/system", "/prompt"]:
                # Allow changing system prompt during conversation
                print("Enter new system prompt:")
                try:
                    new_prompt = input("System: ").strip()
                    if new_prompt:
                        system_prompt = new_prompt
                        # Update the system message
                        messages[0] = {"role": "system", "content": system_prompt}
                        print(f"System prompt updated to: '{system_prompt}'")
                    else:
                        print("System prompt unchanged.")
                except EOFError:
                    print("System prompt unchanged.")
                print("-" * 50)
                continue
            if current_question=='':
                continue
            messages.append({"role": "user", "content": current_question})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            current_response = response.choices[0].message.content
            print(f"Bot: {current_response}")
            bot_responses.append(current_response)
            messages.append({"role": "assistant", "content": current_response})
            questions.append(current_question)
            print('\n'+'-'*50+'\n')
    except EOFError:
        print("\nInteractive chat ended (EOF detected).")
        print("To use interactive chat, run this script in a terminal where you can type input.")
    except KeyboardInterrupt:
        print("\n\nChat ended by user (Ctrl+C).")


if __name__ == "__main__":
    # Set API key - Replace with your actual API key
    # os.environ['OPENAI_API_KEY'] = 'your-openai-api-key-here'
    # Or set it as an environment variable: export OPENAI_API_KEY="your-key-here"
    print("Welcome to ChatGPT Clone!")
    print("Features:")
    print("- Set custom system prompt at startup")
    print("- Change system prompt during chat with '/system' or '/prompt'")
    print("- Type 'exit', 'quit', or 'bye' to end the conversation")
    print("- Press Ctrl+C for emergency exit")
    print("=" * 50)
    interactive_chat()