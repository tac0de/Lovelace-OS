import openai

# Function to handle OpenAI API errors
def handle_api_error(error):
    """
    Handle errors returned by OpenAI API.
    
    Args:
        error (Exception): The exception raised by the OpenAI API.
        
    Returns:
        str: A user-friendly error message.
    """
    print(f"Error encountered: {error}")
    return "Sorry, there was an issue with the AI response. Please try again later."

# Function to format OpenAI API responses
def format_openai_response(response):
    """
    Formats the response from OpenAI API.
    
    Args:
        response (dict): The raw response from the OpenAI API.
        
    Returns:
        str: The formatted response text.
    """
    return response['choices'][0]['message']['content'].strip()
