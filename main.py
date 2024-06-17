import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from llama_index.llms.groq import Groq
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from pdf import pdf_engine
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


llm = Groq(model="mixtral-8x7b-32768", api_key=groq_api_key)
DATA_PATH = "./data"

population_path = os.path.join(DATA_PATH,"WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df = population_df, 
                                            verbose=True,
                                            instruction_str=instruction_str,
                                            llm = llm)
population_query_engine.update_prompts({"pandas_prompt":new_prompt})

# population_query_engine.query("What is the population of India?")

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information for the world population and demographics"
        )
    ),
    QueryEngineTool(
        query_engine=pdf_engine,
        metadata=ToolMetadata(
            name="india_data",
            description="this gives detailed information about India the country"
        )
    )
]

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)

