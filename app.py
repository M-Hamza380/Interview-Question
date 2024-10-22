from src.pipeline.llm_pipeline import LLMPipeline

if __name__ == "__main__":
    llm_pipeline = LLMPipeline()
    answer_chain, questions_list = llm_pipeline.run_llm_pipeline()

    # Generate answers for each question
    for question in questions_list:
        print("-"*50)
        print(f"Question: {question}")
        print("-"*50)
        answer = answer_chain.run(question)
        print(f"Answer: {answer}\n")
        print("-"*50)
    