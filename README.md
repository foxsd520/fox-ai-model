# FoxSD AI Model

**Brand**: FoxSD | **Alias**: Fox | **Contact**: foxsd520@gmail.com

## Overview

FoxSD AI Model is a specialized, production-ready artificial intelligence system designed for:
- 💻 **Programming** - Full software development assistance
- 🔐 **Cybersecurity** - Security consulting and threat analysis
- 🌐 **Web Development** - Modern web application building
- 📱 **App Development** - Mobile and desktop applications
- 🏢 **Business Operations** - Strategic planning and automation

## Architecture

### Core Components

1. **foxsd_model.py** - Intelligent reasoning engine
   - Intent detection with confidence scoring
   - Multi-category classification
   - Smart response generation based on context

2. **database.py** - Persistent data layer
   - Conversation history storage
   - Training data management
   - User profiles and feedback
   - Statistical analysis

3. **chat_engine.py** - Advanced orchestration
   - Session management
   - Memory and context awareness
   - Learning from interactions
   - Training material integration

4. **server.py** - RESTful API
   - FastAPI-based endpoints
   - CORS enabled for cross-origin requests
   - Full documentation at `/docs`

## Installation

### Quick Start

```bash
# Clone repository
git clone https://github.com/foxsd520/fox-ai-model.git
cd fox-ai-model

# Run setup
bash setup.sh

# Start the server
bash start.sh
```

### Manual Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## API Endpoints

### Chat
```
POST /chat
Body: { "text": "your question", "session_id": "optional" }
```

### History
```
GET /history/{session_id}
```

### Training
```
POST /train
Body: {
  "category": "programming",
  "content": "training material",
  "keywords": ["keyword1", "keyword2"]
}
```

### Feedback
```
POST /feedback
Body: {
  "conversation_id": 1,
  "rating": 5,
  "comment": "optional feedback"
}
```

### Statistics
```
GET /stats
```

## Features

✅ **Local-First Design** - All data stays on your server  
✅ **Hybrid Architecture** - Works offline or with external AI models  
✅ **Multi-Domain Expert** - Specialized in programming, security, web/app dev  
✅ **Continuous Learning** - Improves from every interaction  
✅ **Arabic-First** - Full Arabic language support  
✅ **Production Ready** - Secure, scalable, and enterprise-grade  
✅ **Fully Branded** - Only FoxSD branding, no external company references  

## Database Schema

- **conversations** - User and AI interactions
- **training_data** - Knowledge base for continuous learning
- **users** - User accounts and roles
- **feedback** - User ratings and feedback

## File Structure

```
fox-ai-model/
├── foxsd_ai/
│   ├── config.py          # Configuration
│   ├── foxsd_model.py     # Core reasoning engine
│   ├── database.py        # Data persistence
│   ├── chat_engine.py     # Orchestration layer
│   └── server.py          # API server
├── data/                  # SQLite database
├── main.py                # Entry point
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
├── start.sh              # Start script
└── README.md             # This file
```

## Usage

### Start the Server
```bash
python main.py
```
Server runs at `http://localhost:8000`

### API Documentation
```
http://localhost:8000/docs
```

### Python Client Example
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"text": "كيف أبني موقع ويب باستخدام React؟"}
)
print(response.json())
```

## License

MIT License - FoxSD

## Support

For issues and feature requests: foxsd520@gmail.com

---

**Made with ❤️ by FoxSD**  
*Where business intelligence meets practical automation*
