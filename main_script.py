import os
from dotenv import load_dotenv
from openai import OpenAI
from system_promt.py import system_promt

load_dotenv()

# user_input = из телеграм бота приходит

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY_PDD'),
    base_url="https://api.deepseek.com",
)

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

assistant_output = response.choices[0].message.content



