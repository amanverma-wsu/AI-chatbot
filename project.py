import os
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
from datetime import datetime
import random
from geopy.geocoders import Nominatim
from duckduckgo_search import DDGS
import webbrowser
import time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

engine = pyttsx3.init()
engine.setProperty('rate', 170)
stop_requested = False  # For stopping voice + typing

def speak_and_type(text):
    global stop_requested
    stop_requested = False
    chatbox.insert(tk.END, "AI: ", "ai"); chatbox.see(tk.END)
    engine.say(text); engine.startLoop(False)
    for char in text:
        if stop_requested:
            engine.stop(); break
        chatbox.insert(tk.END, char, "ai"); chatbox.see(tk.END)
        root.update(); time.sleep(0.02)
    engine.endLoop()
    chatbox.insert(tk.END, "\n\n")

def stop_speaking():
    global stop_requested
    stop_requested = True

def get_time():
    now = datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}"

def tell_joke():
    jokes = [
        "Why did the computer get cold? Because it left its Windows open!",
        "Why don’t scientists trust atoms? Because they make up everything.",
        "What do you call fake spaghetti? An impasta!",
        "Teacher: Jab mehmaan aate hain to kya karte ho?\nStudent: Remote chhupa deta hoon!",
        "Pappu: Doctor saab, bhoolne ki bimari ho gayi hai.\nDoctor: Kab se?\nPappu: Kab se kya?"
    ]
    return random.choice(jokes)

def search_chatgpt(query):
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error fetching from ChatGPT: {e}"

def get_location_info(place):
    geolocator = Nominatim(user_agent="ai_assistant")
    location = geolocator.geocode(place)
    if location:
        return (f"{place.title()} is located in {location.address}.\n"
                f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        return f"Sorry, I couldn't find location information for '{place}'."

def show_image_result(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.images(query, max_results=1)
            for result in results:
                webbrowser.open(result["image"])
                return f"Showing image result for '{query}'."
        return "No images found."
    except:
        return "Error fetching image."

def process_input(user_input):
    if "time" in user_input:
        return get_time()
    elif "joke" in user_input:
        return tell_joke()
    elif user_input.startswith("where is"):
        place = user_input.replace("where is", "").strip()
        return get_location_info(place)
    elif "show me a picture of" in user_input or "image of" in user_input:
        query = user_input.replace("show me a picture of", "").replace("image of", "").strip()
        return show_image_result(query)
    elif "exit" in user_input or "quit" in user_input:
        root.destroy()
        return "Goodbye!"
    else:
        return search_chatgpt(user_input)

def handle_input():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    entry.delete(0, tk.END)
    chatbox.insert(tk.END, f"You: {user_input}\n", "user")
    response = process_input(user_input.lower())
    speak_and_type(response)

def use_suggestion(text):
    entry.delete(0, tk.END); entry.insert(0, text)
    handle_input()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#1e1e1e")
        chatbox.configure(bg="#252526", fg="white")
        entry.configure(bg="#3c3c3c", fg="white")
        send_button.configure(bg="#3c3c3c", fg="white")
        toggle_button.configure(text="☀️ Light Mode", bg="#3c3c3c", fg="white")
        stop_button.configure(bg="#3c3c3c", fg="white")
    else:
        root.configure(bg="#f0f0f0")
        chatbox.configure(bg="white", fg="black")
        entry.configure(bg="white", fg="black")
        send_button.configure(bg="SystemButtonFace", fg="black")
        toggle_button.configure(text="🌙 Dark Mode", bg="SystemButtonFace", fg="black")
        stop_button.configure(bg="SystemButtonFace", fg="black")

# GUI Setup
root = tk.Tk()
root.title("AI Assistant")
root.geometry("640x700")
dark_mode = False

chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 12))
chatbox.tag_config("user", foreground="#1f6feb", font=("Segoe UI", 12, "bold"))
chatbox.tag_config("ai", foreground="green", font=("Segoe UI", 12))
chatbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

welcome_message = (
    "🤖 Hello! I'm your AI Assistant.\n"
    "I can help with:\n"
    "• 🕒 Time\n• 😂 Jokes\n• 🌐 Ask me anything!\n"
    "• 📍 Location info\n• 🖼️ Image search\n• 🌗 Light/Dark Mode\n"
    "• 🛑 Stop voice or response anytime\n• ⛔ Type 'exit' to close\n\n"
    "👇 Try these:"
)
chatbox.insert(tk.END, welcome_message + "\n\n", "ai")

entry_frame = tk.Frame(root); entry_frame.pack(padx=10, pady=5, fill=tk.X)
entry = tk.Entry(entry_frame, font=("Segoe UI", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", lambda event: handle_input())

send_button = tk.Button(entry_frame, text="Send", font=("Segoe UI", 12), command=handle_input)
send_button.pack(side=tk.RIGHT)

suggestions_frame = tk.Frame(root); suggestions_frame.pack(pady=5)
suggestions = [
    "Tell me a joke", "Where is India?", "What is machine learning?",
    "Show me a picture of the moon", "Who is Albert Einstein?"
]
for text in suggestions:
    btn = tk.Button(suggestions_frame, text=text, font=("Segoe UI", 10),
                    command=lambda t=text: use_suggestion(t))
    btn.pack(side=tk.LEFT, padx=5)

toggle_button = tk.Button(root, text="🌙 Dark Mode", command=toggle_theme); toggle_button.pack(pady=5)
stop_button = tk.Button(root, text="🛑 Stop", font=("Segoe UI", 12), command=stop_speaking); stop_button.pack(pady=5)

speak_and_type("Hello! I'm your AI Assistant. Ask me something.")
root.mainloop()
