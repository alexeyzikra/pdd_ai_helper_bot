import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

with open("glava_1.txt", "r", encoding="utf-8") as f:
    glava_1 = f.read()

# system_promt = "Ты консуульант по ПДД РБ и ... вот текст ПДД" + glava_1 + ...
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

print(response.choices[0].message.content)

