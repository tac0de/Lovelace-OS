import openai
from lovelace_os.core.utils import handle_api_error, format_openai_response  # config에서 import 해야함

# OpenAI API 키 설정
openai.api_key = 'your-openai-api-key-here'

def query_openai(prompt, model="gpt-4o", max_tokens=1000, temperature=0.7):
    """
    OpenAI API에 요청을 보내고 응답을 반환하는 함수
    
    Args:
        prompt (str): 모델에 보낼 질문이나 요청.
        model (str): 사용할 모델 (기본값: gpt-4o).
        max_tokens (int): 응답의 최대 토큰 수.
        temperature (float): 창의성의 정도를 조절 (0.0 ~ 1.0).
    
    Returns:
        str: 모델의 응답
    """
    try:
        response = openai.chat.Completion.create(
            model=model,  # 예: 'gpt-4o'
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return format_openai_response(response)  # 응답 포맷 처리 후 반환
    except Exception as e:
        return handle_api_error(e)  # 오류 처리

# 예시 사용
if __name__ == "__main__":
    prompt = "인공지능의 윤리적 영향에 대해 설명해 주세요."
    print(query_openai(prompt))
