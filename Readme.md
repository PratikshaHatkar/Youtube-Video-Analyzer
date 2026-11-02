# 🎥 AI YouTube Video Analyzer
<img width="1366" height="601" alt="image" src="https://github.com/user-attachments/assets/a06e4c8b-df75-40dd-b1a9-eb13326d3500" />


An AI-powered YouTube Video Analyzer that analyzes YouTube videos and generates structured analysis reports using Large Language Models (LLMs). It extracts video information, identifies important topics, creates meaningful timestamps, and summarizes key learning points.

The application uses **Agno AI Agent**, **Groq LLM**, and **YouTubeTools** to analyze video content through a simple and interactive Streamlit interface.

## ✨ Features

- **YouTube Video Analysis:** Analyze videos by providing a YouTube URL.
- **Video Overview:** Identify video type, duration, metadata, and content structure.
- **Timestamp Generation:** Generate meaningful timestamps for important topics and sections.
- **Content Summarization:** Organize video content into detailed summaries.
- **Topic Identification:** Identify major themes and track topic progression.
- **Key Learning Points:** Highlight important concepts, demonstrations, and references.
- **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
- **AI-Powered Analysis:** Uses Groq LLM through the Agno Agent framework.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Agno | AI Agent framework |
| Groq | Large Language Model provider |
| OpenAI GPT-OSS 20B | Language model used through Groq |
| YouTubeTools | YouTube video analysis tools |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
Youtube-Video-Analyzer/
│
├── app.py
├── youtube_analyzer.py
├── .env
├── .gitignore
└── README.md
```

- `app.py` – Streamlit application that accepts YouTube URLs and displays analysis reports.
- `youtube_analyzer.py` – Creates and configures the AI agent with Groq LLM and YouTubeTools.
- `.env` – Stores API credentials securely.
- `.gitignore` – Excludes sensitive and unnecessary files.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the Project Directory

```bash
cd Youtube-Video-Analyzer
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit agno groq python-dotenv
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Note:** Never share your API key or upload your `.env` file to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🚀 How to Use

1. Launch the application using Streamlit.
2. Enter a valid YouTube video URL in the input field.
3. Click the **Analyze Video** button.
4. Wait while the AI agent processes the video.
5. View the generated analysis report.

## 🧠 AI Agent Workflow

1. The user provides a YouTube video URL through the Streamlit interface.
2. The Streamlit application passes the URL to the Agno AI Agent.
3. The agent uses YouTubeTools to retrieve and analyze available video content.
4. Groq LLM processes the retrieved information.
5. The agent generates a structured report containing:
   - Video overview
   - Important timestamps
   - Topic-wise summaries
   - Key learning points
   - Important references
6. The analysis report is displayed in the Streamlit application.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to access the Groq language model |

## 📌 Future Enhancements

- Generate downloadable PDF reports.
- Support multiple YouTube video analysis.
- Add question-answering functionality for analyzed videos.
- Generate concise summaries for lengthy videos.
- Add transcript-based search functionality.
- Improve timestamp navigation and video segment references.

## 👩‍💻 Author

**Pratiksha Hatkar**

- GitHub: [PratikshaHatkar](https://github.com/PratikshaHatkar)
- LinkedIn: [Pratiksha Hatkar](https://www.linkedin.com/in/pratiksha-hatkar-445815292/)

---

⭐ If you find this project useful, consider giving it a star!
