from typing import List
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import TokenTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain


def llm_pipeline(file_path: str):
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

