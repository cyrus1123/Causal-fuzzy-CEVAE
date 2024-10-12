
from fastapi import FastAPI
from pydantic import BaseModel

class PreprocessingService:
    def __init__(self):
        self.app = FastAPI()

    def setup_routes(self):
        @self.app.post("/preprocess")
        async def preprocess(data: PreprocessRequest):
            processed_data = self.process_data(data.message)
            return {"preprocessed_message": processed_data}

    def process_data(self, message: str):
        # Apply your custom windowing or feature extraction here
        return f"Processed: {message}"

class PreprocessRequest(BaseModel):
    message: str

preprocessing_service = PreprocessingService()
app = preprocessing_service.app
