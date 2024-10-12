
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Chatbot:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()

    def setup_routes(self):
        @self.app.post("/chat", response_model=ChatResponse)
        async def chat_endpoint(chat_request: ChatRequest):
            user_message = chat_request.message
            response = self.generate_response(user_message)
            return ChatResponse(response=response)

    def generate_response(self, message: str) -> str:
        return f"Echo: {message}"

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

chatbot = Chatbot()
app = chatbot.app
