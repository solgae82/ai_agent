import requests
from utils import llm_call

# 요약 함수 선언
def summarize_text(text, feedback_history=None):

    if feedback_history: 
        prompt =(
            f"아래 내용을 요약해줘.\n"
            f"## 원문: {text}\n"
            f"## 이전 요약문 및 피드백 전체 기록:\n{feedback_history}\n\n"
            f"이전 피드백을 모두 참고해 평가 결과가 PASS가 되도록 요약문을 생성해."
        )
    else:  
        prompt = f"아래 내용을 요약해줘.\n원문: {text}"
   
    summary = llm_call(prompt)
    return summary

# 평가 기준 프롬프트 생성
EVALUATOR_PROMPT ="""
평가 기준에 따라 다음 요약문을 엄격하게 심사해.

1. 형식: 
- 여러 항목으로 된 개조식이어야 하며, 한 문장이라도 개조식이 아니면 무조건 FAIL.

2. 내용: 
- 정의 또는 원리, 주요 장점, 활용 예 등 3가지 핵심 요소가 모두 포함되면 PASS.
- 사소한 세부 내용, 인용, 부연 설명 누락은 FAIL이 아님.

3. 표현: 
- 모든 항목은 짧고 명확해야 함.
- 불필요한 수식, 반복문, 비문, 맞춤법/띄어쓰기 오류가 2개 이상이면 FAIL.

위 기준 중 하나라도 미달이면 반드시 FAIL을 부여해.

응답 양식: 
- 평가 결과: PASS / FAIL
- 문제점 및 개선 방향: (FAIL인 경우 구체적으로)
"""

# 평가 함수 선언
def evaluate_summary(content, summary): 
    prompt =(
        f"{EVALUATOR_PROMPT}\n\n"
        f"<원문>\n{content}\n\n"
        f"<요약문>\n{summary}"
    )

    return llm_call(prompt)


# 반복 워크플로 함수 선언
def loop_workflow(content, max_retires=5): 
    feedback_history =""
    for i in range(max_retires): 
        summary = summarize_text(content, feedback_history=feedback_history)
        evaluation = evaluate_summary(content, summary)

        print(f"\n요약 결과:\n{summary}\n")
        print(f"\n평가 결과:\n{evaluation}\n")

        if "평가 결과: PASS" in evaluation: 
            print(f"통과!({i+1}) 최종요약 반환\n")
            return summary

        feedback_history += f"\n\n[시도  {i+1}]\n"
        feedback_history += f"- 요약문:\n{summary}\n- 평가 피드백:\n{evaluation}\n"

    print(f"최대 시도({i+1}) 도달. 마지막 요약 반환")
    return summary

if __name__ == "__main__": 

    # 원문 가져오기
    url = "https://raw.githubusercontent.com/dabidstudio/sample_files/refs/heads/main/sample_wiki_text.md"

    content = requests.get(url).text
    print("원문(앞부분):\n",content[:300], "\n...") # 첫 300글자만 출력

    final_summary = loop_workflow(content , max_retires=5)
    print(final_summary)