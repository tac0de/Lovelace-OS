from lovelace_os.core.ai_core import query_openai
from lovelace_os.core.philosophical_core import ethical_decision


def handle_input(user_input):
    """
    Returns the AI response and ethical decision for a given user input.
    
    Args:
        user_input (str): The user's question.
    
    Returns:
        tuple: The AI response and the ethical decision.
    """
    # Generate AI response
    ai_response = query_openai(user_input)
    
    # Generate ethical decision
    ethical_response = ethical_decision(user_input)
    
    return ai_response, ethical_response

def main():
    """Main CLI entry point for lovelace_os."""
    user_input = input("Ask an ethical question: ")
    ai_response, ethical_response = handle_input(user_input)
    print(f"AI Response: {ai_response}")
    print(f"Ethical Decision: {ethical_response}")

# Example usage
if __name__ == "__main__":
    main()
