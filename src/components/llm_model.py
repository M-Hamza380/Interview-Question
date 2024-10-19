from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain

from src.entity.config_entity import ModelConfig, VectorEmbeddingsConfig
from src.components.file_process import FileProcessing
from src.components.prompt import *

class LLMModel:
    def __init__(self, model_config: ModelConfig, 
                 vector_embeddings_config: VectorEmbeddingsConfig,
                 file_processing: FileProcessing) -> None:
        self.model_config = model_config
        self.vector_embeddings_config = vector_embeddings_config
        self.file_processing = file_processing

    def llm_model(self):
        """
            Executes the LLM model pipeline to generate questions and answers from documents.

            This method utilizes the FileProcessing class to fetch documents and answers, sets up
            the LLM model with specified prompts and configurations, and runs a summarization chain 
            to generate questions. It then loads embeddings and a FAISS index for retrieval-based 
            question answering, and finally, creates a RetrievalQA chain to generate answers for the 
            questions.

            Returns:
                tuple: A tuple containing the answer generation chain and a list of questions.

            Raises:
                RuntimeError: If any error occurs during the execution of the LLM model pipeline.
        """
        try:
            doc_questions, doc_answers = self.file_processing.file_processing()

            # Define the LLM model
            model_name = self.model_config.LLM_MODEL_NAME
            llm_question_gen_pipeline = ChatOllama(
                model=model_name,
                temperature=0.3
            )

            prompt_questions = PromptTemplate(
                template=prompt_template,
                input_variables=["text"]
            )

            refine_prompt_questions = PromptTemplate(
                input_variables=["existing_answer", "text"],
                template=refine_template
            )

            ques_chain = load_summarize_chain(
                llm=llm_question_gen_pipeline,
                chain_type="refine",
                verbose=True,
                question_prompt=prompt_questions,
                refine_prompt=refine_prompt_questions
            )

            ques = ques_chain.run(doc_questions)

            folder_path = self.vector_embeddings_config.root_dir
            embeds = OllamaEmbeddings(model=model_name)

            db = FAISS.load_local(file_path=folder_path, embeddings=embeds, allow_dangerous_deserialization=True)

            llm_ans = ChatOllama(
                model=model_name,
                temperature=0.1
            )

            ques_list = ques.split("\n")
            filtered_ques_list = [element for element in ques_list if element.endswith('?') or element.endswith('.')]

            answer_generation_chain = RetrievalQA.from_chain_type(
                llm=llm_ans,
                chain_type="stuff",
                retriever=db.as_retriever()
            )

            ans = answer_generation_chain.run(ques)

            return answer_generation_chain, filtered_ques_list

        except Exception as e:
            raise RuntimeError(f"Error in LLMModel: {e}")
