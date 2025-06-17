import pytest
from core.philosophical_core import ethical_decision

def test_ethical_decision():
    result = ethical_decision("Should I lie to protect someone's feelings?", "utilitarianism")
    assert result == "Choose the option that maximizes overall happiness."
    
    result = ethical_decision("Should I lie to protect someone's feelings?", "deontology")
    assert result == "Follow the rules, regardless of the outcome."
