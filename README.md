# 🚀 LLM Content Generator (FastAPI + LangChain + OpenRouter)

This project is a simple **AI-powered content generator** that creates essays and poems using Large Language Models (LLMs). It integrates FastAPI for backend APIs, LangChain for prompt orchestration, OpenRouter for model access, and Streamlit for a user-friendly frontend.

---

## 📌 Features

* ✍️ Generate essays based on a topic
* 🎵 Generate poems for kids
* ⚡ FastAPI backend with LangServe routes
* 🔗 OpenRouter integration (OpenAI-compatible API)
* 🎨 Streamlit frontend UI
* 📡 REST API endpoints for easy integration

---

## 🏗️ Tech Stack

* **Backend**: FastAPI
* **LLM Framework**: LangChain
* **LLM Provider**: OpenRouter
* **Frontend**: Streamlit
* **Server**: Uvicorn

---

## 📂 Project Structure

```
api/
│
├── app.py          # FastAPI backend
├── client.py       # Streamlit frontend
├── .env            # API keys (not committed)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Manikandanrintimetec/llm-content-generator-fastapi.git
cd llm-content-generator-fastapi/api
```

---

### 2️⃣ Create virtual environment

```
python -m venv bcd
bcd\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set environment variables

Create a `.env` file inside `api/`:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### 🔹 Start Backend (FastAPI)

```
python -m uvicorn app:app --reload
```

---

### 🔹 Start Frontend (Streamlit)

```
python -m streamlit run client.py
```

---

## 🌐 API Endpoints

| Endpoint  | Description       |
| --------- | ----------------- |
| `/openai` | Direct LLM access |
| `/essay`  | Generate essay    |
| `/poem`   | Generate poem     |

Swagger UI:

```
http://localhost:8000/docs
```

---

## 🧠 How It Works

1. User enters a topic in the Streamlit UI
2. Request is sent to FastAPI
3. LangChain formats the prompt
4. OpenRouter calls the LLM
5. Response is returned and displayed

FastAPI is widely used for building high-performance AI APIs due to its async capabilities and speed ([C# Corner][1]).

---

## 📸 Demo

*Add screenshots of your UI here*

---

## 🚀 Future Improvements

* 💬 Chat-style interface
* 🔄 Streaming responses
* 🎯 Model selection (GPT / Claude / Mixtral)
* 🌍 Deployment (Render / Railway)

---

## ⚠️ Important Notes

* Do NOT upload `.env` file to GitHub
* Add `.env` to `.gitignore`
* Use your own OpenRouter API key

---

## 👨‍💻 Author

**Manikandan R**


