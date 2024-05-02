from flask import Flask, render_template, request, jsonify  # Import necessary Flask components
import openai  # Import OpenAI library
import os

app = Flask(__name__)  # Create a Flask application instance

# Define the OpenAI API key (replace with your actual key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the route for the chatbot conversation
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    user_message = request.get_json()["message"]

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        model="chat",
        prompt=user_message,
        temperature=0.7,
        max_tokens=1000,
    )

    # Extract the generated response from the API response
    bot_message = response["choices"][0]["text"]

    # Return the response as JSON
    return jsonify({"bot_message": bot_message})

# Define the route for the main chat interface
@app.route("/")
def index():
    return render_template("index.html")  # Replace with your actual template name

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode
