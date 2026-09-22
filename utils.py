from openai import AsyncOpenAI, OpenAI
import os

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') # # OS 환경변수 OPENAI_API_KEY 값 가져오기

sysc_client = OpenAI(
    api_key = OPENAI_API_KEY
)

# llm 호출 함수
def llm_call(prompt: str, model: str = 'gpt-4o-mini') -> str: 
    messages = []
    messages.append({'role': 'user', 'content': prompt})

    chat_completion = sysc_client.chat.completions.create(
        model=model,
        messages=messages
    )

    return chat_completion.choices[0].message.content

# 비동기 클라이언트 생성
async_client = AsyncOpenAI(
    api_key = OPENAI_API_KEY
)

# 비동기 LLM 호출 함수 선언
async def llm_call_async(prompt: str, model: str = "gpt-4o-mini") -> str: 
    messages = []
    messages.append({"role":"user", "content": prompt})
    chat_completion = await async_client.chat.completions.create(
        model = model,
        messages= messages
    )

    print(model , "비동기 llm_calll_async 완료")

    return chat_completion.choices[0].message.content


# 모듈이 아닌 main으로 호출할때..
if __name__ == "__main__": 
    test = llm_call("한국 수도는?")
    print(test)
