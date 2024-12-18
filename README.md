# Interview-Question

#### Project Description:

The Interview Question Creator is an advanced generative AI application designed to generate tailored interview questions automatically. Utilizing the power of the LangChain framework, the Ollama(model=llama3.2:1b) model for natural language processing, using OllamaEmbeddings(model=llama3.2:1b), for splitting text using TokenTextSplit(model=gpt-3.5-turbo), and FAISS for efficient data storage in local system, this project serves as a valuable resource for both interviewers and job seekers. The application is built with FastAPI for seamless backend operations, HTML, and JS for an interactive user interface, and is deployed on AWS EC2 for cloud accessibility.


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

