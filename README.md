# V.E.D. AI (Vastly Evolved Digital Intelligence)
### Personalized Chief of Staff for Mr. Surya

V.E.D. is a high-performance AI assistant designed with an Iron Man-inspired HUD and a modular backend.

## 🚀 Features
- **Brain:** Groq Llama 3 for near-instant responses.
- **Voice:** High-fidelity speech using `edge-tts`.
- **Job Agent:** Selenium-based automation for job applications.
- **Automation:** System control and WhatsApp integration.
- **GUI:** Modern Desktop HUD built with CustomTkinter.

## 🛠️ Installation
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/VED-AI.git`
2. Install dependencies: `pip install -r Requirements.txt`
3. Configure `.env` with your Groq/Cohere API keys.
4. Run: `python Main.py`

## ▶️ Demo
Run a simple demo without the GUI:
```bash
python demo.py
```

## 📁 Repository Structure
```
VED-AI/
├── .env
├── .gitignore
├── LICENSE
├── Main.py
├── Requirements.txt
├── README.md
├── demo.py
├── Backend/
│   ├── __init__.py
│   ├── Automation.py
│   ├── Chatbot.py
│   ├── ImageGeneration.py
│   ├── JobApply.py
│   ├── Model.py
│   ├── RealtimeSearch.py
│   ├── SpeechToText.py
│   ├── TextToSpeech.py
│   └── WhatsApp.py
├── Frontend/
│   ├── __init__.py
│   └── GUI.py
└── tests/
    ├── __init__.py
    └── test_decision_layer.py
```

## 🔧 Notes
- Add your API keys to `.env` before running for full Groq/Cohere support.
- When API keys are missing or placeholders are present, V.E.D. runs in demo mode with local fallback messages.
- The demo includes the AI/chatbot route and the image generation stub.
- Use `python demo.py` to verify the system works without GUI.

## 📌 GitHub Setup Instructions
1. Create Repo: Go to GitHub and create a new repository named `VED-AI`.
2. Local Init: In your project folder, run:
    ```bash
git init
git add .
git commit -m "Initialize V.E.D. Intelligence System"
git branch -M main
git remote add origin https://github.com/vickysingh009/VED-AI.git
git push -u origin main
```

The framework is ready, Mr. Surya. All modules are connected and waiting for your API keys to breathe life into the system. 🔵
