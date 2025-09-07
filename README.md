# 🤖 AI Assistant (Python + Tkinter)

A feature-rich **desktop AI Assistant** built with **Python** and **Tkinter**.  
This app combines **OpenAI’s ChatGPT** with local utilities like **time, jokes, location info, and image search** — all wrapped in a simple desktop interface.  

---

## ✨ Features

- **⏰ Time** → Ask the current time.  
- **😂 Jokes** → Get random jokes (English + Hindi).  
- **💬 ChatGPT** → Ask anything, powered by OpenAI API.  
- **📍 Location Info** → Fetch details with latitude/longitude via Geopy.  
- **🖼 Image Search** → Open the first result directly in your browser.  
- **🎨 Theme Toggle** → Switch between Light 🌞 and Dark 🌙 mode.  
- **🔊 Voice Support** → Text-to-Speech responses.  
- **🛑 Stop Button** → Interrupt long responses.  
- **⛔ Exit Command** → Close app safely by typing “exit” or “quit”.  

---

## 🚀 Quickstart

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Assistant.git
cd AI-Assistant
```

Create and activate a virtual environment:

```bash
python -m venv env
```

- **Windows (PowerShell):**
  ```powershell
  .\env\Scripts\Activate
  ```
- **macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

This project requires an **OpenAI API Key**.  

Set it as an environment variable:

- **Windows (PowerShell):**
  ```powershell
  $env:OPENAI_API_KEY="your_api_key_here"
  ```
- **macOS/Linux:**
  ```bash
  export OPENAI_API_KEY="your_api_key_here"
  ```

⚠️ **Never hardcode your API key** inside `project.py`.

---

## ▶️ Run the Application

```bash
python project.py
```

---

## 📂 Project Structure

```
AI-Assistant/
├── project.py          # Core Tkinter application
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore env/, cache, secrets
└── README.md           # Project documentation
```

---

## 🛡️ Security

- API keys should always be set via **environment variables**.  
- The `.gitignore` prevents accidental commits of `env/` and sensitive files.  

---

## 🤝 Contributing

Pull requests are welcome!  
Ideas to improve:
- Add **voice recognition** (speech-to-text).
- More **fun APIs** (weather, news, quotes).  
- Package the app into a `.exe` for Windows users.  

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  

---
