from src.pipeline.llm_pipeline import LLMPipeline

if __name__ == "__main__":
    llm_pipeline = LLMPipeline()
    answer_chain, questions_list = llm_pipeline.run_llm_pipeline()

    print(answer_chain.run(questions_list))
    