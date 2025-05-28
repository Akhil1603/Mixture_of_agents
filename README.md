# 🧠 Mixture-of-Agents LLM App 🧪

Welcome to **LLM Fusion Hub** — where multiple AI minds come together like an Avengers team for your questions! 🎯🤖

---

## 🚀 What’s This?

A **Streamlit** app that sends your question to a squad of open-source LLM superheroes and then merges their answers into one wise, polished reply! Think of it as AI teamwork on steroids 💪✨.

---

## 🛠️ Features

- 🔐 Secure Together API key input
- 🦸‍♂️ Multiple powerful LLM models answering your question independently
- 🧙‍♂️ Aggregator AI that fuses their answers into a single, clear, and accurate response
- 🕵️‍♀️ Shows each model’s individual take — transparency FTW!
- ⏳ Async processing for speedy replies
- 🎉 Fun and user-friendly UI with neat markdown styling

---

## 💻 How It Works

1. You type a question for the **AI Superteam** 🗣️  
2. The app queries multiple reference models individually:  
   - Qwen/Qwen2-72B-Instruct  
   - meta-llama/Llama-Vision-Free  
   - mistralai/Mixtral-8x22B-Instruct-v0.1  
   - meta-llama/Llama-Vision-Free  
3. It collects their responses — some might disagree 🤔, some might shine ✨  
4. The aggregator model (Mixtral-8x22B-Instruct-v0.1) critically synthesizes these into one refined, reliable answer  
5. You get to see both the individual insights and the ultimate wisdom 🧩➡️🌟

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- Streamlit  
- `together` Python SDK (for Together API)  
- Together API key 🔑 (Get it from [Together AI](https://together.xyz/))

### Installation

1. Clone this repo:
git clone https://github.com/Akhil1603/mixture_of_agents.git
cd mixture_of_agents
Install dependencies:

bash
Copy
Edit
pip install streamlit together asyncio
Run the app:

bash
Copy
Edit
streamlit run mixture_of_agents.py
🧙‍♂️ Usage
Enter your Together API Key (hidden for safety!) 🔐

Ask your burning question for the AI Superteam 🗣️

Hit 🚀 Get Answer and watch the AI alliance spring into action!

Explore each model’s response individually for extra context 🧩

Check out the final aggregated, expert-level answer 🌟

🎉 Sidebar Info
Explains how the app gathers and fuses multiple AI model opinions

Lists the powerhouse LLMs behind the scenes

Made with ❤️ by AI and Streamlit fans

⚠️ Troubleshooting
No API key? You can’t assemble the squad! 🔑

Slow or no response? Check your internet & API quota ⏳

Errors from specific models? The app will notify you with clear messages ❌

🤝 Contributing
Feel free to open issues, suggest new models, or submit pull requests!
AI teamwork is better with friends 🙌

📄 License
MIT License — use it, remix it, make it your own!
