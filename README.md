# Interview-Question

#### Project Description:

The Interview Question Creator is an advanced generative AI application designed to automatically generate tailored interview questions. Utilizing the power of the LangChain framework, the Ollama model for natural language processing, and FAISS for efficient data storage, this project serves as a valuable resource for both interviewers and job seekers. The application is built with FastAPI for seamless backend operations, Streamlit for an interactive user interface, and is deployed on AWS EC2 for cloud accessibility.

# Project Workflows

### Steps:

1. config/config.yaml:
2. constants/__init__.py:
3. entity/config_entity.py:
4. configuration/configuration.py:
5. components/data_ingestion.py:
6. components/data_validation.py:
7. components/vector_embeddings.py:
8. components/file_process.py:
9. components/prompt.py:
10. components/llm_model.py:
11. pipeline/llm_pipeline.py:
12. utils/common.py:
13. app.py:

# How to run?

### Steps:

To begin with this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/M-Hamza380/Interview-Question.git
```

2. Create a virtual environment: (using Python)

```
python -m venv 'your virtual env folder name'
```

3. Active your virtual environment: (using VS Code CMD terminal)

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

