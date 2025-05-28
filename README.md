# Interview-Question

#### Project Overview:

An advanced, production-ready generative AI application that automates the creation of tailored interview questions using cutting-edge Retrieval-Augmented Generation (RAG) techniques. Designed as a scalable, modular, and cloud-deployed system for use by interviewers, HR professionals, and job seekers.

#### Key Features & Architecture:
- LLM & RAG Pipeline:
  - Implemented an end-to-end Retrieval-Augmented Generation system using:
    - LangChain for orchestration.
    - Ollama running llama3:2.1b for both generation and embedding (OllamaEmbeddings).
    - FAISS as the local vector database for efficient semantic retrieval.
  - Applied Python (OOP) principles to construct a data ingestion pipeline, including validation, preprocessing, vector embeddings, and LLM models.
- Backend (API Layer):
  - Developed using FastAPI, with:
    - Asynchronous endpoints for high performance using built-in concurrency.
    - APIRouter for modular API organization.
    - RESTful architecture adhering to clean design principles.
    - MVC (Model-View-Controller) architecture for separation of concerns and scalability.
- Frontend (User Interface):
  - Built using HTML, CSS, Bootstrap, and JavaScript for responsive and interactive design.
- Deployment & Infrastructure:
  - Deployed on AWS EC2 for cloud-based access and scalability.
  - Configured with Docker for consistent environment replication.
  - .env file handling for secure and dynamic configuration.
- Tech Stack Summary:
  - Languages & Frameworks: Python, FastAPI, Flask, HTML, CSS, JS, Bootstrap
  - LLM & Embeddings: LangChain, Ollama (llama3:2.1b), GPT-3.5-Turbo
  - RAG Components: FAISS, ChromaDB, TokenTextSplitter
  - Architecture: REST API, FastAPI with APIRouter, MVC Pattern, async I/O
  - Frontend: HTML/CSS/Bootstrap/JS
  - Deployment: AWS EC2, Docker, .env config.

#### Project Outcome:

A fully functional, cloud-deployed AI system for interview question generation. Architected for extensibility, performance, and ease of integration with additional LLMs or frontend tools. Suitable for enterprise use or further customization in HR tech solutions.

# How to run?

### Steps:

To begin this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/M-Hamza380/Interview-Question.git
```

2. Create a virtual environment: (using Python)

```
python -m venv 'your virtual env folder name'
```

3. Activate your virtual environment: (using VS Code CMD terminal)

```
your virtual env folder name\Scripts\activate
```

4. Update your virtual environment:

```
python -m pip install -U pip setuptools
```

5. Install the required libraries:

```
pip install -r requirements.txt
```

6. Open your terminal in VS Code and run the command:

```
python app.py
```

