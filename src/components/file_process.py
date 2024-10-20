from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from pathlib import Path

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
            pdf_dir = Path(self.data_ingestion_config.root_dir)
            pdf_files = list(pdf_dir.glob("*.pdf"))

            if not pdf_files:
                raise FileNotFoundError("No PDF files found in the data ingestion directory.")

            # Extract the text from the PDF
            questions = ""

            for pdf_file in pdf_files:
                # Load PDF Directory
                loader = PyPDFDirectoryLoader(pdf_file)
                data = loader.load()

                # Check what has been loaded
                print(f"Data loaded from {pdf_file}: {data[:5]}")  # Print data structure

                if not data:
                    print(f"No content found in {pdf_file}")
                    continue  # Skip to the next file

                for page in data:
                    if page.page_content:  # Check if page_content is not None or empty
                        questions += page.page_content
                        print(f"Extracted content: {page.page_content[:200]}")  # Print the first 200 characters
                    else:
                        print("No content in this page.")
            
            model_name = self.model_config.TOKEN_MODEL
            split_questions = TokenTextSplitter(
                model_name = model_name,
                chunk_size = 10000,
                chunk_overlap = 200
            )

            chunk_questions = split_questions.split_text(questions)

            doc_questions = [Document(t) for t in chunk_questions if t.strip() != ""]

            split_ans = TokenTextSplitter(
                model_name = model_name,
                chunk_size = 1000,
                chunk_overlap = 100
            )

            doc_answers = split_ans.split_documents(doc_questions)
            print(f"Document Questions: {doc_questions}, Document Answers: {doc_answers}")
            return doc_questions, doc_answers

        except Exception as e:
            raise RuntimeError(f"Error during file processing: {e}")
