import asyncio
import json
from utils import llm_call

# 오케스트레이터 프로프트 생성 함수 선언
def get_orchestrator_prompt(user_query): 
    return f"""
다음 사용자 질물은 분석한 뒤, 이를 3개 이내의 관련 하위 질문으로 분류해.
결과는 JSON 배열로 출력해.
JSON 배열 안의 각 하위 질문은 다음 형식을 따르는 JSON 객체로 만들어.
[
    {{
        "question": "하위 질문 1"
        "description": "이 하위 질문의 요지와 의도에 대한 설명"
    }},
    {{
        "question": "하위 질문 2"
        "description": "이 하위 질문의 요지와 의도에 대한 설명"
    }}
]

사용자 질문: {user_query}
"""

# 오케스트레이터-워커 워크플로로 실행 함수 선언
async def run_orchestrator_workflow(user_query): 
    orchestrator_prompt = get_orchestrator_prompt(user_query)
    orchestrator_response = llm_call(orchestrator_prompt, model="gpt-4o")

    # LLM 응답 앞뒤에 붙은 ```json{}``` 마크다운 코드 블록 제거
    subtask_list = json.loads(
        orchestrator_response.replace("```json","").replace("```","")
    )

    # 하위 질문 출력
    for i, subtask in enumerate(subtask_list, start=1): 
        print(f"\n--- 하위 질문 {i} ---")
        print("질문:",subtask['question'])
        print("설명:",subtask['description'])


async def main(): 
    user_query = "2026sus AI 서비스는 어떻게 발전했을까?"
    final_output = await run_orchestrator_workflow(user_query)


if __name__ == "__main__": 
    asyncio.run(main())