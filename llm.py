import os
from dotenv import load_dotenv
from openai import OpenAI
from system_promt import system_promt
from config import DEEPSEEK_API_KEY_PDD


client = OpenAI(
    api_key=DEEPSEEK_API_KEY_PDD,
    base_url="https://api.deepseek.com",
)

def ask_llm(user_input):

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_promt},
            {"role": "user", "content": user_input},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )
    
    return response.choices[0].message.content
