import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
videos = [
    {
        "id": "HF001",
        "title": "Chair/Bench Workout",
        "duration": "2+ mins",
        "level": "Beginner",
        "type": "Movement",
        "focus": "Full Body",
        "equipment": "Chair/Bench",
        "link": "https://youtube.com/shorts/MvmoFLbp0lQ"
    }
]

def ask_coach(question):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are the Hype Fitness and Wellness AI assistant coach. 
        You speak in a warm, encouraging and calm tone.
        You help beginners and busy professionals build healthy habits.
        Your philosophy is: start small, stay consistent.
        You have access to this video library: """ + str(videos),
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

print("Hype Fitness AI Coach is ready!")
print("Type 'quit' to exit")
print("-" * 40)

while True:
    question = input("You: ")
    if question.lower() == "quit":
        print("Stay consistent! See you next time!")
        break
    response = ask_coach(question)
    print("\nCoach:", response)
    print("-" * 40)