from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document

from src.entity.config_entity import ModelConfig, DataIngestionConfig

class FileProcessing:
    def __init__(self, model_config: ModelConfig, data_ingestion_config: DataIngestionConfig) -> None:
        self.model_config = model_config
        self.data_ingestion_config = data_ingestion_config

    def file_processing(self):
        """
            Processes the PDF files in the data ingestion directory.

            Returns:
                tuple[list[Document], List[Document]]: A tuple containing the questions and answers documents.
        """
        try:
            pdf_dir = self.data_ingestion_config.root_dir
            pdf_files = [f for f in pdf_dir.glob("*.pdf")]

            if not pdf_files:
                raise FileNotFoundError("No PDF files found in the data ingestion directory.")

            # Extract the text from the PDF
            questions = ""

            for pdf_file in pdf_files:
                # Load PDF Directory
                loader = PyPDFDirectoryLoader(pdf_file)
                data = loader.load()

                for page in data:
                    questions += page.page_content
            
            model_name = self.model_config.TOKEN_MODEL
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

        except Exception as e:
            raise RuntimeError(f"Error during file processing: {e}")
