from typing import List
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import TokenTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain

from src.prompt import *

def file_processing(file_path: str) -> tuple[list[Document], List[Document]]:
    """_summary_

    Args:
        file_path (str): give the pdf directory path

    Returns:
        tuple[list[Document], List[Document]]: this function will return the list of documents
    """

    # Load PDF Directory
    loader = PyPDFDirectoryLoader(file_path)
    data = loader.load()

    # Extract the text from the PDF
    questions = ""

    for page in data:
        questions += page.page_content
    
    model_name = "gpt-3.5-turbo"
    split_questions = TokenTextSplitter(
        model_name = model_name,
        chunk_size = 10000,
        chunk_overlap = 200
    )

    chunk_questions = split_questions.split_text(questions)

    doc_questions = [Document(t) for t in chunk_questions]

    split_ans = TokenTextSplitter(
        model_name = model_name,
        chunk_size = 1000,
        chunk_overlap = 100
    )

    doc_answers = split_ans.split_documents(doc_questions)

    return doc_questions, doc_answers


def llm_pipeline(file_path: str):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """

    doc_questions, doc_answers = file_processing(file_path)

    # Define llm model
    model_name = "llama3.2:1b"

    llm_question_gen_pipeline = ChatOllama(
        model = model_name,
        temperature = 0.3
    )

    prompt_questions = PromptTemplate(
    template = prompt_template,
    input_variables = ["text"]
    )

    refine_prompt_questions = PromptTemplate(
    input_variables = ["existing_answer", "text"],
    template = refine_template
    )

    ques_chain = load_summarize_chain(
    llm = model_name,
    chain_type = "refine",
    verbose = True,
    question_prompt = prompt_questions,
    refine_prompt = refine_prompt_questions
    )

    ques = ques_chain.run(doc_questions)

    foler_path = "./vectorstore"
    index_name = "embeds"

    db = FAISS.load_local(file_path=foler_path, index_name=index_name, allow_dangerous_deserialization=True)

    llm_ans = ChatOllama(
        model = model_name,
        temperature = 0.1
    )

    ques_list = ques.split("\n")

    answer_generation_chain = RetrievalQA.from_chain_type(llm=llm_ans, 
                                               chain_type="stuff", 
                                               retriever=db.as_retriever()
                                            )

    ans = answer_generation_chain.run(ques)

    return answer_generation_chain, ques_list

