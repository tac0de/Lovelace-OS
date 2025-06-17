import pytest
from core.ai_core import query_openai

def test_query_openai():
    response = query_openai("What is the meaning of life?")
    assert response is not None  # Check that the response is not None
    assert isinstance(response, str)  # Check that the response is a string
    assert len(response) > 0  # Ensure the response is not empty
