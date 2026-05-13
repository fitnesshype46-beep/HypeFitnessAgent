import anthropic
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

videos = [
    {"id":"HF001","title":"Chair/Bench Workout","duration":"2+ mins","level":"Beginner","type":"Movement","focus":"Full Body","equipment":"Chair/Bench","link":"https://youtube.com/shorts/MvmoFLbp0lQ"},
    {"id":"HF002","title":"Squats and Incline Pushup Workout","duration":"90 secs","level":"Beginner","type":"Movement","focus":"Full Body","equipment":"Chair/Bench","link":"https://youtu.be/l4sQciRQZnY"},
    {"id":"HF003","title":"No Equipment Full Body Workout","duration":"75 secs","level":"Beginner","type":"Movement","focus":"Full Body","equipment":"None","link":"https://youtu.be/ocSXotIYers"}
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('message', '')
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are the Hype Fitness and Wellness AI assistant coach. You speak in a warm, encouraging and calm tone. You help beginners and busy professionals build healthy habits. Your philosophy is: start small, stay consistent. You have access to this video library: " + str(videos) + " Respond in plain conversational text only. No markdown, no bold, no headers.",
        messages=[{"role": "user", "content": question}]
    )
    return jsonify({"response": message.content[0].text})

@app.route('/')
def home():
    return send_from_directory('.', 'chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
