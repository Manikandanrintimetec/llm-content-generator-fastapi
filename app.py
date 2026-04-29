from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenRouter API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Configure OpenRouter model
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo"  # or any OpenRouter model
)

# Prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5-year-old child with 100 words"
)

# Routes
add_routes(app, model, path="/openai")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model,  
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)