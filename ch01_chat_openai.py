import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

#대화 내역을 저장할 리스트 선언
message_history = []

#대화
while True:
    user_input = input("사용자: ")

    #사용자 질문 히스토리에 추가
    message_history.append({'role':'user', 'content': user_input})

    #API로 사용자 질문 전달
    chat_completion = client.chat.completions.create(
        messages= message_history
        , model= 'gpt-4o'
    )

    #AI 응답
    assistant_response = chat_completion.choices[0].message.content

    #AI응답 히스토리에 추가
    message_history.append({'role':'assistant', 'content':assistant_response})

    print(f'챗봇: {assistant_response}')