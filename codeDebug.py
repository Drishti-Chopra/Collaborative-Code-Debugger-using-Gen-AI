def get_debugging_suggestions(code: str) -> str:
    prompt = PromptTemplate(
        input_variables=["code"],
        template="Analyze the following code for syntax errors, potential bugs, and improvements:\n\n{code}\n\nProvide detailed debugging suggestions."
    )
    # Instantiate the LLM using OpenAI (ensure OPENAI_API_KEY is set in your environment)
    # Initialize ChatOllama model
    
    OLLAMA_SERVER_URL = "127.0.0.1:11434"
    MODEL_NAME = "deepseek-r1"
    llm = ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        base_url=OLLAMA_SERVER_URL,
        # other params...
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    suggestions = chain.run(code)
    return suggestions
