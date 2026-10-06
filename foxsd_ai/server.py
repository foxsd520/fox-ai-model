from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
from foxsd_ai.chat_engine import FoxSDChatEngine

app = FastAPI(
    title="FoxSD AI",
    description="Intelligent business AI for programming, cybersecurity, and application development.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = FoxSDChatEngine()


class ChatRequest(BaseModel):
    text: str
    session_id: Optional[str] = None


class TrainingRequest(BaseModel):
    category: str
    content: str
    keywords: List[str]


class FeedbackRequest(BaseModel):
    conversation_id: int
    rating: int
    comment: Optional[str] = None


@app.get("/")
async def root():
    return {
        "brand": "FoxSD",
        "alias": "Fox",
        "email": "foxsd520@gmail.com",
        "service": "FoxSD AI",
        "version": "1.0.0",
        "status": "online",
        "capabilities": [
            "Programming assistance",
            "Cybersecurity consulting",
            "Web development guidance",
            "Application development support",
        ],
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    session_id = request.session_id or str(uuid.uuid4())
    response = engine.process(session_id, request.text)
    return response


@app.get("/history/{session_id}")
async def get_history(session_id: str):
    history = engine.get_conversation_history(session_id)
    return {"session_id": session_id, "conversations": history}


@app.post("/train")
async def add_training(request: TrainingRequest):
    result = engine.add_training_material(request.category, request.content, request.keywords)
    return result


@app.post("/feedback")
async def submit_feedback(request: FeedbackRequest):
    engine.db.save_feedback(request.conversation_id, request.rating, request.comment)
    return {"success": True, "message": "Feedback saved."}


@app.get("/stats")
async def get_stats():
    return engine.get_stats()
