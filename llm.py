import os
from groq import Groq
from dotenv import load_dotenv
from memory import get_history

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt):
    try:
        full_prompt = f"""
        Conversation so far:
        {get_history()}

        Current input:
        {prompt}
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": full_prompt}],
            model="llama-3.3-70b-versatile"
        )

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        return "⚠️ Something went wrong. Please try again."