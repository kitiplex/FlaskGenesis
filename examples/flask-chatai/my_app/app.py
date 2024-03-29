from flask import Flask, render_template, jsonify, request, Response
import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

GPT_MODEL = "gpt-3.5-turbo"

messages = [{
    "role": "system",
    "content": "You are a helpful assistant. Follow instructions carefully. Answer as concise as possible."
}]


def print_message(role, content):
    print(f'{role.capitalize()} : {content}', end="")


async def chat_completion(prompt):
    messages.append({"role": "user", "content": prompt})

    completion = await client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        temperature=0.8,
        max_tokens=150
    )

    return completion.choices[0].message['content']


def generate():
    while True:
        if messages:
            yield f"data: {jsonify({'GinaBot': messages[-1]['content']})}\n\n"
            messages.pop()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.form['user_message']
        if not user_message:
            raise ValueError("User message cannot be empty.")

        with app.app_context():
            gina_message = asyncio.run(chat_completion(user_message))
        return jsonify({"GinaBot": gina_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/stream')
def stream():
    return Response(generate(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
