from flask import Flask, request, jsonify
# Now you can import from 'core' and other modules
from lovelace_os.core.ai_core import query_openai
from lovelace_os.core.philosophical_core import ethical_decision


app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    
    # Generate AI response and ethical decision
    ai_response = query_openai(question)
    ethical_response = ethical_decision(question)
    
    return jsonify({
        "ai_response": ai_response,
        "ethical_response": ethical_response
    })

if __name__ == "__main__":
    app.run(debug=True)
