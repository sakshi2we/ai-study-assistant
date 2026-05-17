# AI Study Assistant 🎓

An AI-powered web application that helps students learn better using Google Gemini API.

Built with **Flask** (Python backend) + **HTML/CSS/JS** (frontend) + **Gemini API** (AI features).

## Features

- 💡 **Explain Concept** — Get simple explanations with real-world analogies for any topic
- 📝 **Generate Quiz** — Auto-generate 3 MCQ questions to test your understanding
- 📄 **Summarise Text** — Paste notes or articles and get bullet-point key ideas
- 🗺️ **Learning Roadmap** — Get a structured 4-week study plan for any skill

## Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI**: Google Gemini 1.5 Flash API
- **Deployment**: Render (free tier)

## Setup & Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/sakshi2we/ai-study-assistant
cd ai-study-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your Gemini API key
- Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- Create a free API key

### 4. Set your API key
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

Or set it as an environment variable:
```bash
export GEMINI_API_KEY=your_api_key_here
```

### 5. Run the app
```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/explain` | Explain a concept |
| POST | `/api/quiz` | Generate MCQ questions |
| POST | `/api/summarise` | Summarise text |
| POST | `/api/roadmap` | Generate learning roadmap |

### Example Request
```bash
curl -X POST http://localhost:5000/api/explain \
  -H "Content-Type: application/json" \
  -d '{"topic": "REST APIs", "level": "beginner"}'
```

## Deployment on Render

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`
6. Add environment variable: `GEMINI_API_KEY = your_key`
7. Deploy — free tier is sufficient

## Project Structure

```
ai-study-assistant/
├── app.py              # Flask backend + API routes
├── requirements.txt    # Python dependencies
├── README.md
└── templates/
    └── index.html      # Frontend (HTML + CSS + JS)
```

## Author

**Sakshi Mishra** — [github.com/sakshi2we](https://github.com/sakshi2we)
