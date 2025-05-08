from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Define a model for the user input
class UserInput(BaseModel):
    prompt: str
    llm_choice: str

# Endpoint to handle user input and get response from LLM
@app.post("/chat/")
async def chat(input: UserInput):
    # Here you would implement the logic to call the selected LLM
    # For example, using LiteLLM or any other LLM service
    try:
        # Simulated response from LLM
        response = f"Response from {input.llm_choice} for prompt: {input.prompt}"
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server with: uvicorn main:app --reload