from typing import Dict, Any, List
import json
from foxsd_ai.foxsd_model import FoxSDReasoner, PromptIntent
from foxsd_ai.database import FoxSDDatabase


class FoxSDChatEngine:
    """Advanced chat engine that combines reasoning, memory, and learning."""

    def __init__(self):
        self.reasoner = FoxSDReasoner()
        self.db = FoxSDDatabase()
        self.memory = {}

    def process(self, session_id: str, user_text: str) -> Dict[str, Any]:
        """Process user input and generate response."""

        result = self.reasoner.build_answer(user_text)
        intent = result["intent"]
        ai_response = result["answer"]

        conversation_id = self.db.save_conversation(
            session_id=session_id,
            user_msg=user_text,
            ai_response=ai_response,
            intent=intent.topic,
            tags=intent.tags,
        )

        return {
            "success": True,
            "conversation_id": conversation_id,
            "brand": result["brand"],
            "intent": intent,
            "response": ai_response,
            "timestamp": result["timestamp"],
        }

    def get_conversation_history(self, session_id: str) -> List[Dict[str, Any]]:
        """Retrieve conversation history for a session."""
        return self.db.get_conversations(session_id)

    def add_training_material(self, category: str, content: str, keywords: List[str]) -> Dict[str, Any]:
        """Add new training material to improve model."""
        data_id = self.db.add_training_data(category, content, keywords)
        return {
            "success": True,
            "data_id": data_id,
            "category": category,
            "message": "Training data added successfully.",
        }

    def get_stats(self) -> Dict[str, Any]:
        """Get system statistics."""
        stats = self.db.get_statistics()
        return {
            "brand": self.reasoner.brand,
            "stats": stats,
        }
