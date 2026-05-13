# YouTube AI Transcriber

Local AI-powered pipeline for YouTube transcription, academic analysis and knowledge extraction using Faster-Whisper, yt-dlp and offline AI workflows.

---

# Overview

This project provides a fully local pipeline for:

- Downloading YouTube audio
- Extracting speech from videos
- Generating high-quality transcriptions
- Producing TXT transcripts
- Supporting academic and educational workflows
- Preparing future AI/RAG integrations

The system is designed for:

- Researchers
- Professors
- Students
- AI enthusiasts
- Content analysts

---

# Features

## Current Features (Phase 1)

- Local/offline transcription
- YouTube audio download
- Faster-Whisper integration
- Portuguese language support
- TXT transcript export
- Modular architecture
- Virtual environment support (venv)

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main language |
| Faster-Whisper | Speech-to-text |
| yt-dlp | YouTube downloader |
| FFmpeg | Audio processing |
| VSCode | Development environment |
| GitHub | Version control |

---

# Project Structure

```text
youtube-ai-transcriber/
│
├── app/
│   ├── main.py
│   ├── downloader.py
│   ├── transcriber.py
│   └── utils.py
│
├── downloads/
├── transcripts/
├── docs/
├── tests/
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-ai-transcriber.git
```

---

## 2. Enter project folder

```bash
cd youtube-ai-transcriber
```

---

## 3. Create virtual environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate virtual environment

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### CMD

```cmd
venv\Scripts\activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# FFmpeg Installation

Download FFmpeg:

https://www.gyan.dev/ffmpeg/builds/

Extract to:

```text
C:\ffmpeg
```

Add to PATH:

```text
C:\ffmpeg\bin
```

Test installation:

```bash
ffmpeg -version
```

---

# Running the Project

Inside the app directory:

```bash
cd app
python main.py
```

Paste the YouTube URL when requested.

---

# Output

The system generates:

```text
downloads/
transcripts/
```

Transcript files are exported as TXT.

---

# Recommended Whisper Configuration

For CPU-based systems:

```python
device="cpu"
compute_type="int8"
```

Recommended model:

```python
"small"
```

---

# Roadmap

## Phase 1
- Local transcription MVP
- TXT export
- Modular architecture

## Phase 2
- Ollama integration
- AI summarization
- Markdown export

## Phase 3
- Academic RAG pipeline
- Semantic search
- Vector database

## Phase 4
- Streamlit/Antigravity interface
- Multi-video processing
- Knowledge management dashboard

---

# Future Goals

- Automatic lecture generation
- Research assistant workflows
- Educational content extraction
- AI-powered summarization
- Semantic indexing
- Offline LLM integration

---

# Target Audience

- Researchers
- Universities
- Educational institutions
- AI developers
- Knowledge workers

---

# License

MIT License

---

# Acknowledgements

- OpenAI Whisper
- Faster-Whisper
- yt-dlp
- FFmpeg
