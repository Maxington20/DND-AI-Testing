from flask import jsonify, Blueprint
import openai

general_questions_blueprint = Blueprint("general_questions", __name__)

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


@general_questions_blueprint.route('/ask', methods=['POST'])
def general_questions_endpoint(question):
    if not question:
        return jsonify({"error": "Please provide a question in the request body."}), 400
    prompt = f"Answer this D&D 5e question: {question}"
    answer = generate_response(prompt)
    return jsonify({"answer": answer})