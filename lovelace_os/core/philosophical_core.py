def ethical_decision(question, framework="utilitarianism"):
    """
    주어진 윤리적 질문에 대해 선택된 윤리적 이론을 기반으로 결정을 내림.
    
    Args:
        question (str): 윤리적 질문 (예: '거짓말을 해야 할까요?').
        framework (str): 선택된 윤리적 이론 (예: 'utilitarianism' 또는 'deontology').
    
    Returns:
        str: 윤리적 결정을 내린 결과.
    """
    if framework == "utilitarianism":
        return "행복을 극대화하는 선택을 하세요."
    elif framework == "deontology":
        return "규칙을 지키세요, 결과와 관계없이."
    else:
        return "알려지지 않은 윤리적 이론입니다."

# 예시 사용
if __name__ == "__main__":
    question = "어떤 사람을 구하기 위해 다른 사람을 희생해야 할까요?"
    print(ethical_decision(question, "utilitarianism"))
