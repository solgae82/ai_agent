import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY") # OS 환경변수 OPENAI_API_KEY 값 가져오기
)

chat_completion = client.chat.completions.create(

    messages=[
        {
            'role':'user',
            'content':'Say this is a test'
        }
    ],
    model = 'gpt-4o'
)

print(chat_completion.choices[0].message.content)