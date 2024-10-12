
from fastapi.testclient import TestClient
from chatbot import app

class TestChatbotAPI:
    def __init__(self):
        self.client = TestClient(app)

    def test_chat_endpoint(self):
        response = self.client.post("/chat", json={"user_id": "123", "message": "Hello!"})
        assert response.status_code == 200
        assert response.json() == {"response": "Echo: Hello!"}

test_chatbot = TestChatbotAPI()
test_chatbot.test_chat_endpoint()
